import numpy as np
import csv
import matplotlib.pyplot as plt

X = []
y = []

with open ("ex2data2.txt" , "r") as csvfile:
    rowreader = csv.reader(csvfile)
    for row in rowreader:
        row.insert(0,1)
        y.append(row.pop())
        X.append(row)
csvfile.close()

X = np.array(X)
y = np.array(y)
print(y)
