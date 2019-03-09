from statistics import stdev , mean

def clean(X ,m , n):
    for i in range(0,n):
        temp = []
        for j in range(0,m):
            temp.append(X[j][i])
        mu = mean(temp)
        sigma = stdev(temp)
        if sigma == 0 :
            continue
        for j in range(0,m):
            X[j][i] = (X[j][i] - mu)/sigma

