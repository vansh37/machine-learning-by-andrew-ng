import csv
import numpy as np
import costFunction
import cleandata
import matplotlib.pyplot as plt
from math import fabs

X = [] 
Y = []

with open('ex1data2.txt' , 'r') as csvfile:
    rowreader = csv.reader(csvfile)
    for row in rowreader:
        row.insert(0,1)
        Y.append(row.pop())
        X.append(row)
csvfile.close()

####
alpha = 0.01            #learning rate
m = np.shape(X)[0]   # number of rows
n = np.shape(X)[1]   #number of coloumns
theta = []
EPS = 0.01             #LIMIT {difference in J }
for i in range(0,n):
    theta.append(0)

for i in range(0,m):
    for j in range(0,n):
        X[i][j] = int(X[i][j])
    Y[i] = int(Y[i])
cleandata.clean(X,m,n)
#cleandata.clean(Y,m,1)
#print(X)
#print(Y)
####

J_HISTORY = []
J_HISTORY.append(costFunction.cost(X,Y,theta,m,n))

ctr = 400
while True and ctr > 0:

    theta_temp = []
    costarray = []
    
    for i in range(0,m):
        temp  = []
        for j in range(0,n):
            temp.append(X[i][j])
        costarray.append(costFunction.h(temp , theta , n) - Y[i])

    for i in range(0,n):
        temp = 0
        for j in range(0,m):
            temp += costarray[j]*X[j][i]
        theta_temp.append(theta[i] - (alpha/m)*temp)
    
    theta = theta_temp
    J_HISTORY.append(costFunction.cost(X,Y,theta,m,n))

    if fabs(J_HISTORY[-1] - J_HISTORY[-2]) <= EPS:
        break
    ctr = ctr - 1
print (theta)

plt.plot(J_HISTORY)
plt.show()

