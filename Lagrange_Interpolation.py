import numpy as np
import matplotlib.pyplot as plt

x=[1, 3, 5]
y=[1.1, 10, 23.5]


x_lagrange=np.arange(0,10,0.1)
y_lagrange=(187/80)*x_lagrange**2 - (49/10)*x_lagrange + 293/80

plt.plot(x[0],y[0], 'bo',label='P1')
plt.plot(x[1],y[1], 'mo',label='P2')
plt.plot(x[2],y[2], 'ko',label='P3')

plt.plot(x_lagrange,y_lagrange, color='r')
plt.grid()
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
