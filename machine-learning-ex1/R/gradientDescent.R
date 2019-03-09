setwd('/home/vansh/Desktop/machine-learning-by-andrew-ng/machine-learning-ex1/R')
DATA <- read.csv('ex1data2.txt' , header = FALSE , sep = ',')
DATA = as.matrix(DATA)  #idk this had DATA as list and i wasnt able to perform matrix multiplication
# i need to read more into this

### DATA ###
Y <- DATA[,ncol(DATA)]
X <- DATA[,1:ncol(DATA)-1]
alpha = 0.01
n = ncol(X) + 1  #taking account of the 1 coloumn
m = nrow(X)
theta = matrix(0,n,1)
EPS = 0.001
###------###

### applying normalisation ###
for (i in range(1:ncol(X))){
  avg <- mean(X[,i])
  sigma = sd(X[,i])
  X[,i] <- X[,i] - avg
  X[,i] <- X[,i]/sigma
}
###-----------------------###

### adding coloumn of 1 in X ###
X <- cbind(matrix(1,m,1) , X)
###---------------###

costfunction <- function(){
    return ( (1/(2*m)) * ( t(X %*% theta - Y) %*% (X %*% theta - Y) ) )
}
prev <- costfunction()
ctr <- 400
count <- 0
J_HISTORY = c(prev)
repeat{
  theta <- theta - (alpha/m) * ( t(X) %*% (X %*% theta - Y) ) 
  curr <- costfunction()
  if (abs(curr - prev) <= EPS || ctr <= 0){    break
  }
 J_HISTORY <- append(J_HISTORY  , c(curr) , after = length(J_HISTORY))
  ctr <- ctr - 1
  count <- count + 1
  prev <- curr  
}
# theta
# curr
# count 
 plot(J_HISTORY)
# theta[1] + 1650*theta[2] + 3*theta[3]
# 
theta

