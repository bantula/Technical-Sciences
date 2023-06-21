import pandas as pd
import matplotlib.pyplot as plt
import csv

df = pd.read_csv('googleplaystore1.csv')

app = []
category = []
rating = []
reviews = []
size = []
installs = []
type = []
price = []
content_rating = []
genres = []
last_updated = []
current_version = []
android_version = []


with open('googleplaystore1.csv', encoding="utf8") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        app.append(row[0])
        category.append(row[1])
        rating.append(row[2])
        reviews.append(row[3])
        size.append(row[4])
        installs.append(row[5])
        type.append(row[6])
        price.append(row[7])
        content_rating.append(row[8])
        genres.append(row[9])
        last_updated.append(row[10])
        current_version.append(row[11])
        android_version.append(row[12])

try:
    for i in range (len(app)):
        rating[i] = float(rating[i])
        reviews[i] = float(reviews[i])
except:
    rating[i] = 0

x = rating
y = reviews


plt.scatter(x, y, 10)
plt.xlabel('rating')
plt.ylabel('reviews')
plt.figure(figsize=(5,10))
#plt.title('')
plt.show()