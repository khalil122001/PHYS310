import numpy as np 

def bisection_method(f,x1,x2,e):
    if f(x1)*f(x2) >=0:
        return print('No root exists in these boundaries')
    x1_n=x1 
    x2_n=x2
    while (x2_n - x1_n) < e:
        mid = (x1_n + x2_n) / 2
        f_mid = f(mid)
        if f(x1_n) * f_mid < 0:
            x2_n = mid
        elif f(x2_n) * f_mid < 0:
            x1_n = mid
        elif f_mid == 0:
            return print('Exact solution found: ',mid)
        else: 
            return print('Method Failed')
    return print((x1_n + x2_n) / 2)

def f(x):
    return np.sin(x)
def df(x):
    return np.cos(x)
bisection_method(f,np.pi/2,1.5*np.pi,0.001)

def Newton_Raphson(f,df,x,e):
    h = f(x) / df(x)
    while abs(h) > e:
        h=f(x) / df(x)
        x = x - h
        print(x)
    print('The root found is: ',x)

Newton_Raphson(f,df,np.pi/4,0.0001)