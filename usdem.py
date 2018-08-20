from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
import csv


white = [233657078]
black = [40241818]
nativeamerican = [2597817]
asian = [16614625]
other = [15133856]
mixedrace = [9752947]
hispanic = [56500000]
labels = 'White', 'Black', 'Native American', 'Asian', 'Other', 'Mixed Race', 'Hispanic'
sizes = [76.6, 13.4, 1.3, 5.8, 0.2, 2.7, 17.8]
explode = (0, 0.1, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("US Demographics by Race")
plt.show()
