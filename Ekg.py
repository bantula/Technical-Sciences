import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
from scipy.io import wavfile

Fs, data = wavfile.read('C:\\Users\\Windows User\\Documents\\PFE\\training\\training-a\\a0007.wav')


def filterDesign_bandpass1(Fth_L, Fth_H, fs, order):
    f_max = 0.5 * fs
    low_cutoff = Fth_L / f_max
    high_cutoff = Fth_H / f_max
    b, a = butter(5, [low_cutoff, high_cutoff], btype='bandpass')
    return b, a


def bandpass_filter(data, Fth_L, Fth_H, fs, order):
    b, a = filterDesign_bandpass1(Fth_L, Fth_H, fs, order)
    y = lfilter(b, a, data)
    return y


Fth_L1 = 30
Fth_H1 = 200

y1 = bandpass_filter(data, Fth_L1, Fth_H1, Fs, 5)

Fth_L2 = 10
Fth_H2 = 600

y2 = bandpass_filter(data, Fth_L2, Fth_H2, Fs, 8)
t = np.linspace(0, np.size(data) / Fs, np.size(data))

i = 0
j = 0
n = 10
a = []
while i <= np.size(y1):
    a.append(np.mean(y1[j * n:(j + 1) * n]))
    j = j + 1
    i = i + n

a = np.array(a)
a = np.diff(a) * -1

d = a * 0;
e = a * 0;
maxA = 1500
margin = 30
c = maxA + 1

while c > maxA:
    b = np.argmax(a)
    c = a[b]
    d[b] = c
    a[b - margin:b + margin] = 0

T = np.array(np.zeros(np.size(d)))
R = np.array(np.zeros(np.size(d)))

RT = np.array(np.zeros(np.size(d)))
TR = np.array(np.zeros(np.size(d)))

m = 0
n = len(d)
br1 = 0
br2 = 0
br3 = 0
br4 = 0

for k in range(0, np.size(d)):
    if d[k] > 0:
        if d[k] < 6000:
            T[br1] = k
            if ((br2 != 0) and (abs(br2 - br1) <= 1)):
                br3 = br3 + 1;
                RT[br3] = -1 * R[br2 - 1] + T[br1]
            br1 = br1 + 1
        else:
            R[br2] = k
            if ((br1 != 0) and (abs(br2 - br1) <= 1)):
                br4 = br4 + 1;
                TR[br4] = -1 * T[br1 - 1] + R[br2]
            br2 = br2 + 1

vreme = np.size(d) * 10 / Fs
broj_otkucaja = (br1 + br2) // 2
broj_otkucaja_u_minuti = round(((br1 + br2) // 2 / vreme) * 60)
br_R_zubaca = br1
br_T_zubaca = br2
korektnih_RT_prelaza = br3
korektnih_TR_prelaza = br4
prosecan_broj_RT_prelaza = np.mean(RT)
prosecan_broj_TR_prelaza = np.mean(TR)
srednje_odstupanje_od_prosecnog_RT_perioda = np.mean(abs((RT - np.mean(RT))))
procentualno_odstupanje_od_prosecnog_RT_perioda = np.mean(abs((RT - np.mean(RT)))) / np.mean(RT) * 100
srednje_odstupanje_od_prosecnog_TR_perioda = np.mean(abs((TR - np.mean(TR))))
procentualno_odstupanje_od_prosecnog_TR_perioda = np.mean(abs((TR - np.mean(TR)))) / np.mean(TR) * 100

print("Snimanje je trajalo:", vreme)
print("Detektovano je:", broj_otkucaja, "otkucaja");
print("U minutu je bilo:", broj_otkucaja_u_minuti, "otkucaja");
print("Detektovano je:", br_R_zubaca, " R zubaca");
print("Detektovano je:", br_T_zubaca, " T zubaca");
print("Korektnih RT prelaza je bilo :", korektnih_RT_prelaza);
print("Korektnih TR prelaza je bilo :", korektnih_TR_prelaza);
print("Proseca RT period je bio :", prosecan_broj_RT_prelaza);
print("Proseca TR period je bio :", prosecan_broj_TR_prelaza);
print("Srednje odstupanje od prosecnog RT perioda je bilo :", srednje_odstupanje_od_prosecnog_RT_perioda);
print("Procentualno odstupanje od prosecnog RT perioda je bilo :", procentualno_odstupanje_od_prosecnog_RT_perioda, "%")
print("Srednje odstupanje od prosecnog TR perioda je bilo :", srednje_odstupanje_od_prosecnog_TR_perioda);
print("Procentualno odstupanje od prosecnog TR perioda je bilo :", procentualno_odstupanje_od_prosecnog_TR_perioda, "%")

if broj_otkucaja_u_minuti == 0:
    print("Bolest srca: Asistola")

if broj_otkucaja_u_minuti < 60 and broj_otkucaja_u_minuti > 0:
    print("Bolest srca: Bradikardija")

if broj_otkucaja_u_minuti > 100:
    print("Bolest srca: Tahikardija")
elif broj_otkucaja_u_minuti > 120 and broj_otkucaja_u_minuti < 200:
    print("Ventrikularna tahikardija")
elif broj_otkucaja_u_minuti > 120 and broj_otkucaja_u_minuti < 250:
    print("Supraventrikularna tahikardija")
elif broj_otkucaja_u_minuti > 400 and broj_otkucaja_u_minuti < 600:
    print("Atrialna fibrilacija")
elif broj_otkucaja_u_minuti > 250 and broj_otkucaja_u_minuti < 350:
    print("Atril flutter")
elif broj_otkucaja_u_minuti > 400:
    print("Vertikularna fibrilacija")

if broj_otkucaja_u_minuti > 60 and broj_otkucaja_u_minuti < 100:
    print("Nema aritmiju")

plt.plot(data)
plt.show()
