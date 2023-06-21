import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = input("File name: ")
img = Image.open(img)

v_cele = img.height
s_cele = img.width

plt.imshow(img)
plt.show()


def is_white(t):
    pix_val = list(t)
    if(pix_val[1] >= 200 and pix_val[2] >= 200 and pix_val[3] >= 200):
        return True

x1 = 0
y1 = 0

for y in range(img.height):
    for x in range(img.width):
        pixel = img.getpixel((x, y))
        if not is_white(pixel):
            x1 = x
            y1 = y
            break

    if x1 != 0 or y1 != 0:
        break

crna_linija = [[x1, y1]]
i = 0
while i < (len(crna_linija)):
    currx = crna_linija[i][0]
    curry = crna_linija[i][1]

    if not is_white(img.getpixel((currx + 1, curry))):
        if [currx + 1, curry] not in crna_linija:
            crna_linija.append([currx + 1, curry])
    if not is_white(img.getpixel((currx - 1, curry))):
        if [currx - 1, curry] not in crna_linija:
            crna_linija.append([currx - 1, curry])
    if not is_white(img.getpixel((currx, curry + 1))):
        if [currx, curry + 1] not in crna_linija:
            crna_linija.append([currx, curry + 1])
    if not is_white(img.getpixel((currx, curry - 1))):
        if [currx, curry - 1] not in crna_linija:
            crna_linija.append([currx, curry - 1])

    i = i + 1

pixels = img.load()  # create the pixel map

for pt in crna_linija:
    pixels[pt[0], pt[1]] = 255  # change to white

max = crna_linija[-1][1]

d_linije = max - y1
p_pixela = (5 / d_linije) * (5 / d_linije)

plt.imshow(img)
plt.show()

count = 0
for y in range(img.height):
    for x in range(img.width):
        pixel = img.getpixel((x, y))
        if pixel >= 200:
            count += 1

print(count, " pixels are bright.")

# image1 = plt.imread(input("File name: "))
# image1 = np.array(image1)

blacky = (v_cele * s_cele) - count
povrsina = blacky * p_pixela
print(povrsina, " cm^2")
