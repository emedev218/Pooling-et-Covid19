## Faux-positifs


from math import *
from matplotlib.pyplot import plot, show, legend
import numpy as np
import matplotlib.pyplot as plt

#formule de la borne inférieure
def borne(n,eps,p):
    return (np.log(eps/(1-eps))+np.log(p/(1-p)))/(np.log(1-(1-p)**(n-1)))


#borne inf en fonction de n, à epsilon fixé
nb=[i for i in range (1, 200)]  #nb de tests disponibles

a=[borne(n,0.5,0.005) for n in nb]
a1=[borne(n,0.5,0.002) for n in nb]
a2=[borne(n,0.5,0.001) for n in nb]

b=[borne(n,0.25,0.005) for n in nb]
b1=[borne(n,0.25,0.002) for n in nb]
b2=[borne(n,0.25,0.001) for n in nb]

c=[borne(n,0.1,0.005) for n in nb]
c1=[borne(n,0.1,0.002) for n in nb]
c2=[borne(n,0.1,0.001) for n in nb]

d=[borne(n,0.01,0.005)for n in nb]
d1=[borne(n,0.01,0.002) for n in nb]
d2=[borne(n,0.01,0.001) for n in nb]

e=[borne(n,0.001,0.005) for n in nb]
e1=[borne(n,0.001,0.002) for n in nb]
e2=[borne(n,0.001,0.001) for n in nb]

f=[borne(n,0.0001,0.005) for n in nb]
f1=[borne(n,0.0001,0.002) for n in nb]
f2=[borne(n,0.0001,0.001) for n in nb]

plt.figure()
plt.subplot(231)
plot(nb,a, label='$p=5\%$')
plot(nb,a1,label='$p=1\%$')
plot(nb,a2,label='$p=0.1\%$')
plt.xlabel('$n$')
plt.ylabel('borne inférieure de $L$')
plt.title('$\epsilon$=0.5')
legend()

plt.subplot(232)
plot(nb,b, label='$p=0.5\%$')
plot(nb,b1,label='$p=0.2\%$')
plot(nb,b2,label='$p=0.1\%$')
plt.xlabel('$n$')
plt.ylabel('borne inférieure de $L$')
plt.title('$\epsilon$=0.25')
legend()


plt.subplot(233)
plot(nb,c, label='$p=0.5\%$')
plot(nb,c1,label='$p=0.2\%$')
plot(nb,c2,label='$p=0.1\%$')
plt.xlabel('$n$')
plt.ylabel('borne inférieure de $L$')
plt.title('$\epsilon$=0.1')
legend()


plt.subplot(234)
plot(nb,d, label='$p=0.5\%$')
plot(nb,d1,label='$p=0.2\%$')
plot(nb,d2,label='$p=0.1\%$')
plt.xlabel('$n$')
plt.ylabel('borne inférieure de $L$')
plt.title('$\epsilon$=0.01')
legend()
plt.subplot(235)
plot(nb,e, label='$p=0.5\%$')
plot(nb,e1,label='$p=0.2\%$')
plot(nb,e2,label='$p=0.1\%$')
plt.xlabel('$n$')
plt.ylabel('borne inférieure de $L$')
plt.title('$\epsilon$=0.001')
legend()

plt.subplot(236)
plot(nb,f, label='$p=0.5\%$')
plot(nb,f1,label='$p=0.2\%$')
plot(nb,f2,label='$p=0.1\%$')
plt.xlabel('$n$')
plt.ylabel('borne inférieure de $L$')
plt.title('$\epsilon$=0.0001')
legend()
show()

 
