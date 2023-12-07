import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import random

def density(x1, x2, beta):
    #return (1 / np.sqrt(2 * np.pi * beta)) * np.exp((x1 - x2)**2 / (2 * beta))
    den = np.zeros((len(x1),len(x2)))
    for i in range(len(x1)):
        for j in range(len(x2)):
            den[i,j] = (1 / np.sqrt(2 * np.pi * beta)) * np.exp(-(x1[i] - x2[j])**2 / (2 * beta))
    return den

def harmonic(x, beta, k):
    return np.exp(-0.5 * k * x) * density(x, x, beta) * np.exp(-0.5 * k * x)

x = np.linspace(0,1,1000)
beta = 0.01
k = .005
dx = x[1]-x[0]
h = harmonic(x,beta,k)

for _ in range(5):
    plt.imshow(h)
    plt.show()
    h = h*h * dx
plt.imshow(h)
plt.show()
'''

## Harmonic Path 

def rho(x1,x2,beta):
    return (1 / np.sqrt(2 * np.pi * beta)) * np.exp(-(x1 - x2)**2 / (2 * beta))

def randomeWalk(x,beta,d):
    N = len(x)
    delta = beta / N
    k = np.random.randint(0,N-2)
    k_plus = k +1
    k_minus = k - 1
    if k_minus == -1: k_minus = N-1
    x_k = x[k] + random.uniform(-d,d)
    pi_a = rho(x[k_minus],x[k],delta) * rho(x[k], x[k_plus], delta) * np.exp(-0.5 * delta * x[k]**2)
    pi_b = rho(x[k_minus],x_k,delta) * rho(x_k, x[k_plus], delta) * np.exp(-0.5 * delta * x_k**2)
    if random.uniform(0,1) < pi_b/pi_a:
        x[k] = x_k
    return x


x = np.linspace(0,1,1000)
beta = 4
d = 0.1
for i in tqdm(range(10000000)):
    x = randomeWalk(x,beta,d)

plt.hist(x,bins=80, weights= 1/np.full(len(x),len(x)))
plt.show()
'''