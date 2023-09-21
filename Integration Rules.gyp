import numpy as np 
from scipy.integrate import quad
import matplotlib.pyplot as plt 

x1 = 0
x2 = np.pi 
n=100
h= (x2 - x1) / (n-1 )
x = np.linspace(x1,x2,n)
func = np.sin(x) #+ np.random.random(n)

# Trapizoidal Rule 

I_trapizoid = (h/2) * (func[0] + func[n-1]) + np.sum(func[1:n-1]) * h
print(I_trapizoid)
plt.plot(x,func)
plt.show()

# Simpson's Rule 

I_simpson = (h/3) * (func[0] + func[n-1]) + (2*h/3) * (np.sum(func[:n-2:2])) + (4*h/3) * (np.sum(func[1:n-1:2]))
print(I_simpson)

# Python integrator 

def f(x):
    return np.sin(x)

I_package = quad(f,x1,x2)
print(I_package)