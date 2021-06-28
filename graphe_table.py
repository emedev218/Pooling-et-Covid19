##Démonstration du résultat de Thompson

from math import*
import random
import scipy.special
from matplotlib.pyplot import plot, show, legend
import numpy as np
import matplotlib.pyplot as plt

def esp(p,N,n):
    S=0
    for i in range (0,n+1):
        S=S+(i/n)**(1/N)*scipy.special.binom(n,i)*(1-(1-p)**N)**(n-i)*(1-p)**(N*i)
    return 1-S

## évolution du biais en fonction de n (p,N fixés)
def biais (p,N,n):
    return esp(p,N,n)-p

x=[i for i in range(1,20)]
y=[biais(0.01,2,a) for a in range(1,20)]
y1=[biais(0.01,5,a) for a in range(1,20)]
y2=[biais(0.01,10,a) for a in range(1,20)]
y3=[biais(0.05,2,a) for a in range(1,20)]
y4=[biais(0.05,5,a) for a in range(1,20)]
y5=[biais(0.05,10,a) for a in range(1,20)]
y6=[biais(0.1,2,a) for a in range(1,20)]
y7=[biais(0.1,5,a) for a in range(1,20)]
y8=[biais(0.1,10,a) for a in range(1,20)]
y9=[biais(0.5,2,a) for a in range(1,20)]
y10=[biais(0.5,5,a) for a in range(1,20)]
y11=[biais(0.5,10,a) for a in range(1,20)]
plt.figure(1)

plt.subplot(221)
plot(x,y, label='$N=2$')
plot(x,y1,label='$N=5$')
plot(x,y2,label='$N=10$')
plt.ylabel('Biais')
plt.xlabel('nombre de pools ($n$)')
plt.title('$p^*=0.01$')
legend()
plt.subplot(222)
plot(x,y3,label='$N=2$')
plot(x,y4,label='$N=5$')
plot(x,y5,label='$N=10$')
plt.ylabel('Biais')
plt.xlabel('nombre de pools ($n$)')
plt.title('$p^*=0.05$')
legend()

plt.subplot(223)
plot(x,y6,label='$N=2$')
plot(x,y7,label='$N=5$')
plot(x,y8,label='$N=10$')
plt.ylabel('Biais')
plt.xlabel('nombre de pools ($n$)')
plt.title('$p^*=0.1$')
legend()

plt.subplot(224)
plot(x,y9,label='$N=2$')
plot(x,y10,label='$N=5$')
plot(x,y11,label='$N=10$')
plt.ylabel('Biais')
plt.xlabel('nombre de pools ($n$)')
plt.title('$p^*=0.5$')
legend()
show()

## variance asymptotique

def varianceas(p,N,n):
    return (1-(1-p)**N)/(n*N**2*(1-p)**(N-2))

## risque
def variance(p,N,n):
    S=0
    for i in range (0,n+1):
        S=S+(i/n)**(2/N)*scipy.special.binom(n,i)*(1-(1-p)**N)**(n-i)*(1-p)**(N*i)

    return S -(1-esp(p,N,n))**2

def risque(p,N,n):
    return variance(p,N,n)+(biais(p,N,n))**2

def diff(p,N,n):
    return abs(risque(p,N,n)-varianceas(p,N,n))

n=[i for i in range (1,20)]

r=[ diff(0.01,2,a) for a in n]
r1=[ diff(0.01,5,a) for a in n]
r2= [ diff(0.01,10,a) for a in n]
r3=[ diff(0.05,2,a) for a in n]
r4=[ diff(0.05,5,a) for a in n]
r5=[ diff(0.05,10,a) for a in n]
r6=[ diff(0.1,2,a) for a in n]
r7=[ diff(0.1,5,a) for a in n]
r8=[ diff(0.1,10,a) for a in n]
r9=[ diff(0.5,2,a) for a in n]
r10=[ diff(0.5,5,a) for a in n]
r11=[ diff(0.5,10,a) for a in n]

plt.figure(2)

plt.subplot(221)
plot(n,r, label='$N=2$')
plot(n,r1, label='$N=5$')
plot(n,r2, label='$N=10$')
plt.xlabel('nombre de pools ($n$)' )
plt.ylabel('différence entre risque quadratique  \n et variance asymptotique')
plt.title('$p^*=0.01$')
legend()

plt.subplot(222)

plot(n,r3, label='$N=2$')
plot(n,r4, label='$N=5$')
plot(n,r5, label='$N=10$')
plt.xlabel('nombre de pools ($n$)' )
plt.ylabel('différence entre risque quadratique  \n et variance asymptotique')
plt.title('$p^*=0.05$')
legend()

plt.subplot(223)

plot(n,r6, label='$N=2$')
plot(n,r7, label='$N=5$')
plot(n,r8, label='$N=10$')
plt.xlabel('nombre de pools ($n$)' )
plt.ylabel('différence entre risque quadratique  \n et variance asymptotique')
plt.title('$p^*=0.1$')
legend()
plt.subplot(224)

plot(n,r9, label='$N=2$')
plot(n,r10, label='$N=5$')
plot(n,r11, label='$N=10$')
plt.xlabel('nombre de pools ($n$)' )
plt.ylabel('différence entre risque quadratique  \n et variance asymptotique')
plt.title('$p^*=0.5$')
legend()

show()

## fixer n puis faire varier p pour différents N (biais)
z=[i for i in np.arange (0,1, 0.01)]
b1=[1-(1-a)**2-a for a in z]
b2=[1-(1-a)**5-a for a in z]
b3=[1-(1-a)**10-a for a in z]
z1=[biais(a, 2, 10) for a in z]
z2=[biais(a, 5, 10) for a in z]
z3=[biais(a, 10, 10) for a in z]
z4=[biais(a, 2, 20) for a in z]
z5=[biais(a, 5, 20) for a in z]
z6=[biais(a, 10, 20) for a in z]
z7=[biais(a, 2, 100) for a in z]
z8=[biais(a, 5, 100) for a in z]
z9=[biais(a, 10, 100) for a in z]
z10=[biais(a, 2, 1000) for a in z]
z11=[biais(a, 5, 1000) for a in z]
z12=[biais(a, 10, 1000) for a in z]
plt.figure()
plt.subplot(221)
plot(z,b1, "b--")
plot(z,b2, "r--")
plot(z,b3, "g--")
plot (z,z1, color='blue', label='$N=2$')
plot(z,z2, color='red', label='$N=5$')
plot(z,z3, color='green', label='$N=10$')
plt.xlabel('Prévalence ($p^*$)')
plt.ylabel('Biais')
legend()
plt.title('$n=10$')

plt.subplot(222)
plot(z,b1, "b--")
plot(z,b2, "r--")
plot(z,b3, "g--")
plot (z,z4,color='blue', label='$N=2$')
plot(z,z5,color='red', label='$N=5$')
plot(z,z6, color='green',label='$N=10$')
plt.xlabel('Prévalence ($p^*$)')
plt.ylabel('Biais')
legend()
plt.title('$n=20$')
plt.subplot(223)
plot(z,b1, "b--")
plot(z,b2, "r--")
plot(z,b3, "g--")
plot (z,z7,color='blue', label='$N=2$')
plot(z,z8,color='red', label='$N=5$')
plot(z,z9, color='green',label='$N=10$')
plt.xlabel('Prévalence ($p^*$)')
plt.ylabel('Biais')
legend()
plt.title('$n=100$')

plt.subplot(224)
plot(z,b1, "b--")
plot(z,b2, "r--")
plot(z,b3, "g--")
plot (z,z10,color='blue', label='$N=2$')
plot(z,z11,color='red', label='$N=5$')
plot(z,z12, color='green',label='$N=10$')
plt.xlabel('Prévalence ($p^*$)')
plt.ylabel('Biais')
legend()
plt.title('$n=1000$')
show()

## fixer n puis faire varier p pour différents N (risque-variance)
s1=[diff(a,2,10) for a in z]
s2=[diff(a,5,10) for a in z]
s3=[diff(a,10,10) for a in z]
s4=[diff(a,2,20) for a in z]
s5=[diff(a,5,20) for a in z]
s6=[diff(a,10,20) for a in z]
s7=[diff(a,2,100) for a in z]
s8=[diff(a,5,100) for a in z]
s9=[diff(a,10,100) for a in z]

plt.figure()
plt.subplot(221)
plot (z,s1, label='$N=2$')
plot(z,s2, label='$N=5$')
plot(z,s3, label='$N=10$')
plt.xlabel('Prévalence ($p^*$')
plt.ylabel('Différence entre risque quadratique  \n et variance asymptotique')
legend()
plt.title('$n=10$')

plt.subplot(222)
plot (z,s4, label='$N=2$')
plot(z,s5, label='$N=5$')
plot(z,s6, label='$N=10$')
plt.xlabel('Prévalence ($p^*$)')
plt.ylabel('Différence entre risque quadratique  \n et variance asymptotique')
legend()
plt.title('$n=20$')

plt.subplot(223)
plot (z,s7, label='$N=2$')
plot(z,s8, label='$N=5$')
plot(z,s9, label='$N=10$')
plt.xlabel('Prévalence ($p^*$)')
plt.ylabel('Différence entre risque quadratique  \n et variance asymptotique')
legend()
plt.title('$n=100$')
show()




##

N=[i for i in range(1,20)]
n1=[risque(0.1, a, 2) for a in N]
n2=[risque(0.1, a, 5) for a in N]
n3=[risque(0.1, a, 10) for a in N]
n4=[risque(0.1, a, 20) for a in N]
n5=[risque(0.1, a, 40) for a in N]
n6=[risque(0.1, a, 100) for a in N]

plot(N,n1, label='$n=2$')
plot(N,n2,label='$n=5$')
plot(N,n3,label='$n=10$')
plot(N,n4,label='$n=20$')
plot(N,n5,label='$n=40$')
plot(N,n6,label='$n=100$')
plot(np.argmin(n1), np.min(n1), "b.", label='$n=2$')
plot(np.argmin(n2), np.min(n2), "r.", label='$n=5$')
plot(np.argmin(n3), np.min(n3), "g.", label='$n=10$')

plot(np.argmin(n4), np.min(n4), "m.", label='$n=20$')
plot(np.argmin(n5), np.min(n5), "y.", label='$n=40$')
plot(np.argmin(n6), np.min(n6), "c.", label='$n=100$')
plt.xlabel('taille des pools ($N$)')
plt.ylabel('valeur minimale du risque quadratique')
plt.title ('$p=0.1$')
legend()
plt.show()


def tailleopt(p):
    return int((1.59)/(-np.log(1-p)))


prev=[i for i in np.arange(0.5,1,0.01)]
Nopt=[tailleopt(p) for p in prev]
n1=[risque(0.5, a, 2) for a in N]
n2=[risque(0.5, a, 5) for a in N]
n3=[risque(0.5, a, 10) for a in N]
n4=[risque(0.5, a, 20) for a in N]
n5=[risque(0.5, a, 40) for a in N]
n6=[risque(0.5, a, 100) for a in N]
plot(N,n1)
plot(N,n2)
plot(N,n3)
plot(N,n4)
plot(N,n5)
plot(N,n6)
plt.xlabel('taille de pool')
plt.ylabel('risque qudratique')
show()
plot(prev,Nopt)
show()
fig, axe1_X = plt.subplots()
axe2_X = axe1_X.twinx()
axe1_X.plot(prev, Nopt, 'r-')
axe2_X.plot(prev, n1, 'b-')
axe1_X.set_xlabel('prévalence $p^*$')
axe1_X.set_ylabel('taille de pool optimale',color='red')
axe2_X.set_ylabel('risque quadratique pour $p^*=0.5$', color='blue')
plt.title('p=1%')
show()

print('La prévalence est p=0.5 et la taille de pool optimale associée est', tailleopt(0.5))
print('--------------------')
print('un sur-estimateur de la prévalence est',random.uniform(0.5,1), '\n', 'et la taille de pool optimale est', tailleopt(random.uniform(0.5,1)))
print('--------------------')
print('un sous-estimateur de la prévalence est',random.uniform(0,0.5), '\n', 'et la taille de pool optimale est', tailleopt(random.uniform(0,0.5)))


n=10000
for i in range(1,21):
    print(i, risque(0.1,i,n))