import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from scipy.interpolate import interp1d
# Starting with the manual Interpolation 

x2=np.array([1, 3, 5])
y2=np.array([0.8, 10, 23.5])

x_lagrange=np.arange(0,10,0.1)

def lagrange_interpol(x,x2, y2):
    P1 = (y2[0]*(x-x2[1])*(x-x2[2]))/((x2[0]-x2[1])*(x2[0]-x2[2]))
    P2 = (y2[1]*(x-x2[0])*(x-x2[2]))/((x2[1]-x2[0])*(x2[1]-x2[2]))
    P3 = (y2[2]*(x-x2[0])*(x-x2[1]))/((x2[2]-x2[0])*(x2[2]-x2[1]))
    y = P1 + P2 + P3
    return y

x1= np.arange(0,10, 0.1)
y1 = np.array([])
for i in x1:
    y1  = np.append(y1, lagrange_interpol(i,x2,y2))

plt.plot(x2[0],y2[0], 'bo',label='P1')
plt.plot(x2[1],y2[1], 'mo',label='P2')
plt.plot(x2[2],y2[2], 'ko',label='P3')
plt.plot(x1,y1, color='r')
plt.grid()
plt.legend()
plt.title('Lagrange Interpolation of y=x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# Newton/Atkins Method And Quadratic Splines
def Atkins_method(x,x1,y1):
    p12 = (x-x1[1])/(x1[0] - x1[1]) * y1[0] + (x-x1[0])/(x1[1]-x1[0]) * y1[1]
    p23 = (x-x1[2])/(x1[1] - x1[2]) * y1[1] + (x-x1[1])/(x1[2]-x1[1]) * y1[2]
    p34 = (x-x1[3])/(x1[2] - x1[3]) * y1[2] + (x-x1[2])/(x1[3]-x1[2]) * y1[3]
    p123 = (x-x1[2])/(x1[0] - x1[2]) * p12 + (x-x1[0])/(x1[2]-x1[0]) * p23
    p234 = (x-x1[3])/(x1[1] - x1[3]) * p23 + (x-x1[1])/(x1[3]-x1[1]) * p34
    p1234 = (x-x1[3])/(x1[0] - x1[3]) * p123 + (x-x1[0])/(x1[3]-x1[0]) * p234
    return p1234

# Modeling equation f(x) = 1/1+x

x_f=np.array([1, 2, 3, 4])
y_f=np.array([0.45, 0.35, 0.23, 0.18])

x_r=np.linspace(np.min(x_f),np.max(x_f),50)
y_quadratic = interp1d(x_f, y_f, kind='quadratic')
y_r=np.array([])
for i in x_r:
    y_r = np.append(y_r,Atkins_method(i,x_f,y_f))
y_real=1/(1+x_r)
plt.figure()
plt.plot(x_f[0],y_f[0], 'bo',label='P1')
plt.plot(x_f[1],y_f[1], 'mo',label='P2')
plt.plot(x_f[2],y_f[2], 'ko',label='P3')
plt.plot(x_f[3],y_f[3], 'ro',label='P4')
plt.plot(x_r,y_r, color='b',label='Atkins Interpolation')
plt.plot(x_r,y_real,color='k',label='Real Function')
plt.plot(x_r,y_quadratic(x_r),color='m',label='Quadratic Splines')
plt.grid()
plt.legend()
plt.title('Atkins Method for Interpolating y=1/1+x')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# Scipy Python Library for Lagrange Function
f_lag= lagrange(x_f,y_f)
plt.figure
plt.plot(x_r,f_lag(x_r), 'g' , x_f, y_f , 'mo')
plt.plot(x_r,y_real,color='k')
plt.grid()
plt.legend()
plt.title('Lagrange Interpolation of y=x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
