from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
import csv

open ("fatal-police-shootings-data.csv")
csvFile = open("fatal-police-shootings-data.csv", "r")
csvReader = csv.reader(csvFile, delimiter= ',')
black = 0
white = 0
asian = 0
hispanic = 0
data=0
armed = 0
unarmed = 0
other = 0
undetermined= 0
#for i in csvReader:
    #if i[0] == 'id':
        #continue
    #del i[0]
    #data.append(i)

#print(data)

for row in csvReader:
    if row[7]== 'A':
        asian+=1
    if row[7] == 'B':
        black += 1
    if row[7] == 'W':
        white +=1
    if row[7] == "H":
        hispanic += 1

    if row[4] == 'gun' or row[4] == 'machete' or row[4] == 'gun and knife' or row[4] == 'ax' or row[4] == 'hatchet' :
        armed +=1
    if row[4] == 'unarmed' or row[4] == 'toy weapon':
        unarmed +=1
    if row[4] == 'undetermined':
        undetermined +=1
    else:
        other +=1

print(armed)
print(unarmed)
print(other)


#What is the Race of Poele killed by the Police
x = np.arange(4)
amount = [hispanic, black, asian, white]
colors=["lightpink", "yellowgreen", "red", "cyan"]
plt.bar(x, amount, color=colors)
plt.xticks(x, ('Hispanic', 'Black', 'Asian', 'White'))
plt.title("Race of the People Killed by Police Since Jan 1. 2015")
plt.xlabel("Race")
plt.ylabel("Number of Deaths")
plt.show()


#How many people were armed with 'deadly' weapons

x = np.arange(4)
kamount = [armed, unarmed, other, undetermined]
kcolors = ["red", "blue", "purple", "black"]
plt.bar(x, kamount, color = kcolors)
plt.xticks(x, ('Armed', 'Unarmed', 'Other', 'Undetermined'))
plt.title("How Many People Were Armed With 'Deadly' Weapons")
plt.xlabel("Weapon")
plt.ylabel("Number of People Who Died")
plt.show()
