##Faux-négatifs

from math import *
from matplotlib.pyplot import plot, show, legend
import numpy as np
import matplotlib.pyplot as plt
def g(n,p,x):
    return (1-p*(1-x))**(n-1)

def fauxneg(L,n,p,x):   #formule du taux de faux-neg
    return L*(1-g(n,p,x))**(L-1)

#taux de faux-neg en fonction de la charge, pour différents L,p,n
charge=[i for i in np.arange(0,1,0.01)]
a=[fauxneg(3,6,0.005,i) for i in charge]
b=[fauxneg(3,6,0.002,i) for i in charge]
c=[fauxneg(3,6,0.001,i) for i in charge]

d=[fauxneg(3,8,0.005,i) for i in charge]
e=[fauxneg(3,8,0.002,i) for i in charge]
f=[fauxneg(3,8,0.001,i) for i in charge]

a1=[fauxneg(4,61,0.005,i) for i in charge]
b1=[fauxneg(4,61,0.002,i) for i in charge]
c1=[fauxneg(4,61,0.001,i) for i in charge]

e1=[fauxneg(7,61,0.005,i) for i in charge]
f1=[fauxneg(7,61,0.002,i) for i in charge]
g1=[fauxneg(7,61,0.001,i) for i in charge]


plt.figure()
plt.subplot(221)
plot(charge,a, label='$p=0.5\%$')
plot(charge,b, label='$p=0.2\%$')
plot(charge,c, label='$p=0.1\%$')
plt.ylim(0,0.0035)
plt.xlabel('charge $x$')
plt.ylabel('borne supérieure pour \n le taux de faux-négatifs')
plt.title('$n=6,L=3$')
legend()

plt.subplot(222)
plot(charge,d, label='$p=0.5\%$')
plot(charge,e, label='$p=0.2\%$')
plot(charge,f, label='$p=0.1\%$')
plt.xlabel('charge $x$')
plt.ylabel('borne supérieure pour \n le taux de faux-négatifs')
plt.title('$n=8,L=3$')
legend()

plt.subplot(223)
plot(charge,a1, label='$p=0.5\%$')
plot(charge,b1, label='$p=0.2\%$')
plot(charge,c1, label='$p=0.1\%$')
plt.xlabel('charge $x$')
plt.ylabel('borne supérieure pour \n le taux de faux-négatifs')
plt.title('$n=61,L=4$')
legend()

show()

plt.subplot(224)
plot(charge,e1, label='$p=0.5\%$')
plot(charge,f1, label='$p=0.2\%$')
plot(charge,g1, label='$p=0.1\%$')
plt.ylim(0,0.07)
plt.xlabel('charge $x$')
plt.ylabel('borne supérieure pour \n le taux de faux-négatifs')
plt.title('$n=61,L=7$')
legend()

show()



