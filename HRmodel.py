'''
Created on May 2, 2014

@author: sun
'''

N=10000
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    X=np.zeros((0))
    Y=np.zeros((0))
    Z=np.zeros((0))
    x=0;y=0;z=0
    a=1;b=3;c=1;d=5;s=4;r=0.006;xhi=-1.6;
    I=3;dt=0.1
    for j in range(N):
        xn=x+(y-a*x**3+b*x**2-z+I)*dt
        yn=y+(c-d*x**2-y)*dt
        zn=z+r*(s*(x-xhi)-z)*dt
        x=xn;y=yn;z=zn;
        X=np.append(X,x);Y=np.append(Y,y);Z=np.append(Z,z);
    plt.plot(X)
    plt.show()
        
