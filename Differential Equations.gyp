import numpy as np 
import scipy as sp 
import math
import matplotlib.pyplot as plt 
import sympy as sy 

# Euler Method 
# Defining an ODE with exponential growth dy/dt = y 
'''
def f(t,y):
    return y

def euler(f,y0,t): # where f is the function, y0 is the initial condition, and t is the time interval
    y=np.zeros(len(t))
    y[0] = y0
    h = t[1] - t[0]
    for i in range(0,len(t) - 1):
        y[i+1] = y[i] + h*f(t[i],y[i])
    return y

y0=1
t=np.linspace(0,2,20)

y_soln= euler(f,y0,t)
y1= np.exp(t)
plt.plot(t, y_soln,label='Euler Estimate')
plt.plot(t,y1,label='Actual Solution')
plt.legend()
plt.xlabel('t')
plt.ylabel('y')
plt.grid()
plt.title('Graphing ODE Estimate of dy/dt=y usig the euler mnethod')
plt.show()
# To get the error 
print(np.sum((y_soln - y1)**2))

# Range-Kutta 2 Method 
def RK2(f,y0,t):
    y=np.zeros(len(t))
    y[0] = y0
    h= t[1] - t[0]
    for i in range(0,len(t) - 1):
        k1 = h * f(t[i],y[i])
        k2 = h * f(t[i] + 0.5*h,y[i] + 0.5*k1)
        y[i+1] = y[i] + k2
    return y

# Range-Kutta 4 Method 
def RK4(f,y0,t):
    y=np.zeros(len(t))
    y[0] = y0
    h= t[1] - t[0]
    for i in range(0,len(t)-1):
        k1=h*f(t[i],y[i])
        k2=h*f(t[i]+0.5*h,y[i]+0.5*k1)
        k3=h*f(t[i]+0.5*h,y[i]+0.5*k2)
        k4=h*f(t[i]+h,y[i]+k3)
        y[i+1] = y[i] + (1/6)*(k1+2*k2+2*k3+k4)
    return y

plt.figure()
y_soln= euler(f,y0,t)
y_soln1= RK2(f,y0,t)
y_soln2= RK4(f,y0,t)
y1= np.exp(t)
plt.plot(t, y_soln,'r*',label='Euler Estimate')
plt.plot(t, y_soln1,'bo',label='RK2 Estimate')
plt.plot(t, y_soln2,'k^',label='Rk4 Estimate')
plt.plot(t,y1,'m*',label='Actual Solution')
plt.legend()
plt.xlabel('t')
plt.ylabel('y')
plt.grid()
plt.title('Graphing ODE Estimate of dy/dt=y using all three mnethod')
plt.show()

print('Euler', np.sum((y_soln - y1)**2),'\n')
print('RK2',np.sum((y_soln1 - y1)**2),'\n')
print('RK4',np.sum((y_soln2 - y1)**2),'\n')



# Simple Harmonic Oscillator
# Euler Method 
t=np.linspace(0,10,1000)
y=np.zeros(len(t))
v=np.zeros(len(t))
h=t[1]-t[0]
y[0]=10
v[0]=-2
for i in range(0,len(t)-1):
    y[i+1] = y[i] + h*v[i]
    v[i+1] = v[i] + h*(10*np.cos(2*np.pi*t[i]))
plt.figure()
plt.plot(t,y)
plt.show()
plt.figure()
plt.plot(t,v)
plt.show()

# RK 2 Method 
# y' = v
# v' = f cos(wt) - w^2y 
f=3
w=2
def F(y,v,t):
    return f*np.cos(w*t) - (w**2)*y
t=np.linspace(0,10,100)
ypoints=[]
vpoints=[]
h=t[1]-t[0]
y=2
v=2
for i in range(0,len(t)):
    ypoints.append(y)
    vpoints.append(v)

    m1 = h*v
    k1 = h*F(y, v, t[i])  

    m2 = h*(v + 0.5*k1)
    k2 = h*F(y+0.5*m1, v+0.5*k1, t[i]+0.5*h)

    y += m2
    v += k2

plt.plot(t,ypoints)
plt.show()
plt.figure
plt.plot(t,vpoints)
plt.show()
'''
# RK 4 Method 
# y' = v
# v' = f cos(wt) - w^2y 
f=3
w=2
def F(y,v,t):
    return f*np.cos(w*t) - (w**2)*y
t=np.linspace(0,10,100)
ypoints=[]
vpoints=[]
h=t[1]-t[0]
y=2
v=2
for i in range(0,len(t)):
    ypoints.append(y)
    vpoints.append(v)

    m1 = h*v
    k1 = h*F(y, v, t[i])  

    m2 = h*(v + 0.5*k1)
    k2 = h*F(y+0.5*m1, v+0.5*k1, t[i]+0.5*h)

    m3 = h*(v + 0.5*k2)
    k3 = h*F(y+0.5*m2, v+0.5*k2, t[i]+0.5*h)

    m4 = h*(v + k3)
    k4 = h*F(y+m3, v+k3, t[i]+h)

    y += (m1 + 2*m2 + 2*m3 + m4)/6
    v += (k1 + 2*k2 + 2*k3 + k4)/6

plt.plot(t,ypoints)
plt.xlabel('Time t (s)')
plt.ylabel('Position y (m)')
plt.grid()
plt.title('Evolution of position of a forced Pendulum')
plt.show()
plt.figure
plt.plot(t,vpoints)
plt.xlabel('Time t (s)')
plt.ylabel('Velocity v (m/s)')
plt.title('Evolution of velocity of a forced Pendulum')
plt.grid()
plt.show()
