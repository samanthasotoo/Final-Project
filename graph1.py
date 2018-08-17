from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
import csv

open ("fatal-police-shootings-data.csv")
csvFile = open("fatal-police-shootings-data.csv", "r")
csvReader = csv.reader(csvFile, delimiter= ',')
black = []
white = []
asian = []
hispanic = []
for row in csvReader:
     print(row[1])
