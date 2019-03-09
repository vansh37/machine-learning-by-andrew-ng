def h (x ,theta, n):
    s = 0
    for i in range(0,n):
        s += x[i]*theta[i]
    return s



def cost(X, Y, theta, m, n):
    c = 0
    for i in range(0,m):
        temp = []
        for j in range(0,n):
            temp.append(X[i][j])
        c += (h(temp , theta , n) - Y[i]) * (h(temp , theta , n ) - Y[i])
    c *= (1/(2*m))
    return c

