import numpy as np 
from scipy import optimize
import matplotlib.pyplot as plt

# generating data of equation y = 2x + 3 with errors
x= np.linspace(0,20,50)
n=len(x)
y= 2*x + 3 + 10* np.random.random(n)

# Physically getting the least squares through the sums equations 

xbar = np.mean(x)
ybar = np.mean(y)

num = 0
den = 0
for i in range(n):
    num += (x[i] - xbar) * (y[i] - ybar)
    den += (x[i] - xbar) ** 2
m = num/den # slope 
b = ybar - (m * xbar) # y-intercept 
print(m, b)
y_reg = m*x + b
plt.plot(x,y,'r*',label='Data Point')
plt.plot(x,y_reg,color='b',label='Linear Regression')
plt.title('Least Square Approximation of y = 2x + 3')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()

# Writing it in Matrix formation
A= np.vstack([x,np.ones(len(x))]).T
y = y[:,None] # changing y into a column vector
alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)),y) # Getting 
print(alpha)
plt.figure()
plt.plot(x,y,'r*',label='Data Point')
plt.plot(x,alpha[0]*x + alpha[1],color='b',label='Linear Regression')
plt.legend()
plt.grid()
plt.show()

# Using optimize.curve_fit from scipy 
def func(x,m,b):
    y=m*x + b
    return y

beta = optimize.curve_fit(func,xdata=x,ydata=y)[0]
print(beta)