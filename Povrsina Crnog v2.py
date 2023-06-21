# import numpy as np
# import matplotlib as plt
import cv2

img = input("File name: ")
img = cv2.imread(img) #ubacis sliku u ovaj folder i za input uneses tacan naziv slike
                      #obavezno mora da bude .png jer ne radi jpg

cv2.imshow('slika', img)
cv2.waitKey(0)
cv2.destroyAllWindows() #ovo koristis da prikazes sliku

img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
t = 50
for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        if img[i, j] < t:
            img[i, j] = 0
        else:
            img[i, j] = 255

cv2.imshow('slika', img)
cv2.waitKey(0)
cv2.destroyAllWindows() #ovo ti je binarizacija, t ti je treshold

def is_white(pixel):
    return pixel <= 200 #proverava da li je piksel beo

x1 = 0
y1 = 0
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        pixel = img[x, y]
        if not is_white(pixel):
            x1 = x
            y1 = y
            break

    if x1 != 0 or y1 != 0:
        break                     #ovime trazimo prvi crni piksel koji pripada crnoj liniji
                                # do ovde mi je sve radilo normalno
crna_linija = [[x1, y1]]

i = 0
while i < (len(crna_linija)):
    currx = crna_linija[i][0]
    curry = crna_linija[i][1]

    if not is_white(img[currx + 1, curry]):
        if [currx + 1, curry] not in crna_linija:
            crna_linija.append([currx + 1, curry])
    if not is_white(img[currx - 1, curry]):
        if [currx - 1, curry] not in crna_linija:
            crna_linija.append([currx - 1, curry])
    if not is_white(img[currx, curry + 1]):
        if [currx, curry + 1] not in crna_linija:
            crna_linija.append([currx, curry + 1])
    if not is_white(img[currx, curry - 1]):
        if [currx, curry - 1] not in crna_linija:
            crna_linija.append([currx, curry - 1])

    i = i + 1
    # trazili smo duzinu crne linije

for pt in crna_linija:
    crna_linija[[pt[0], pt[1]]] = 255  # obojimo liniju u belo

max = crna_linija[-1][1]

d_linije = max - y1
p_pixela = (5 / d_linije) * (5 / d_linije)  #linija je duzine 5 cm kad je povlacimo na papiru

cv2.imshow('slika', img)
cv2.waitKey(0)
cv2.destroyAllWindows() # ovo mi nije radilo, program samo ide i ne prekida se, ne prikazuje nikakvu gresku

count = 0
for y in range(img.height):
    for x in range(img.width):
        pixel = img[x, y]
        if pixel >= 200:
            count += 1

print(count, " pixels are bright.") #brojimo sve bele piksele

blacky = (img.shape[0] * img.shape[1]) - count #dobijemo broj crnih piksela
povrsina = blacky * p_pixela
print(povrsina, " cm^2")