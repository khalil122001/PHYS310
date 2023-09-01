import numpy as np
import matplotlib.pyplot as plt

x2=np.array([1, 3, 5])
y2=np.array([1.2, 10, 23.5])

x_lagrange=np.arange(0,10,0.1)

def lagrange_interpol(x,x2, y2):
    P1 = (y2[0]*(x-x2[1])*(x-x2[2]))/((x2[0]-x2[1])*(x2[0]-x2[2]))
    P2 = (y2[1]*(x-x2[0])*(x-x2[2]))/((x2[1]-x2[2])*(x2[1]-x2[2]))
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
print(len(x1))
print(len(y1))
plt.plot(x1,y1, color='r')
plt.grid()
plt.legend()
plt.title('Lagrange Interpolation of y=x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
