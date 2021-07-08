from math import*
import random
from statistics import mean
import scipy.special
from matplotlib.pyplot import plot, show, legend
import numpy as np
import matplotlib.pyplot as plt

##taille de pool optimale déterminée par Thompson
def tailleopt(p):
    if p==0.0:
        return 0
    return int((1.59)/(-np.log(1-p))+0.5)

##calcul de la somme des X_i^{(N)} (v.a de Bernoulli)
def somme(prev,taille,n): #taille=taille du pool (N)
    liste=[]
    S=0
    for i in range(n):
        liste.append(np.random.binomial(1,1-(1-prev)**taille))   #proba qu'un pool de taille N soit positif=1-(1-p)^N
        S=S+liste[i]
    #print(liste)
    return S

##calcul de l'estimateur
def calculesti(prev,taille,n):
    esti=1-((1/n)*somme(prev,taille,n))**(1/taille) #formule de l'estimateur
    return esti

##intervalle de confiance
def infconf(prev,taille,n): #borne inf
    if prev==0.0:
        return 0
    S=somme(prev,taille,n)
    a=prev-(1.96*((1/n)*S)**(1/taille -1)*np.sqrt((1-(1/n)*S)*(1/n)*S))/(taille*np.sqrt(n))
    return a

def supconf(prev,taille,n): #borne sup
    S=somme(prev,taille,n)
    b=prev+(1.96*((1/n)*S)**(1/taille -1)*np.sqrt((1-(1/n)*S)*(1/n)*S))/(taille*np.sqrt(n))
    return b


##estimateurs initiaux p°
estim_ini=[i for i in np.arange(0.001,0.8,0.05)]

###################################### n=20 #########################################
estim_itera=[calculesti(p,tailleopt(p),20) for p in estim_ini]

inf=[infconf(p,tailleopt(p),20)for p in estim_itera]

sup=[supconf(p,tailleopt(p),20)for p in estim_itera]

######################################## n=1000  #######################################
estim_iter1a=[calculesti(p,tailleopt(p),1000) for p in estim_ini]

inf1=[infconf(p,tailleopt(p),1000)for p in estim_iter1a]

sup1=[supconf(p,tailleopt(p),1000)for p in estim_iter1a]

#########################################tracé##################################################
plt.figure(1)
###n=20
plt.subplot(221)
L= [[] for j in range(len(estim_ini))]

for j in range(1,100):
    estim_iter=[calculesti(p,tailleopt(p),20) for p in estim_ini]
    plt.scatter(estim_ini,estim_iter, c='black')
    for i in range (len(L)):
        L[i].append(estim_iter[i])
M=[]
for i in range (0,len(L)):
    M.append(np.percentile(L[i],50))

PQ=[]
for i in range (0,len(L)):
    PQ.append(np.percentile(L[i],25))

DQ=[]
for i in range (0,len(L)):
    DQ.append(np.percentile(L[i],75))

C=[]
for i in range (0,len(L)):
    C.append(np.percentile(L[i],97.5))

plot(estim_ini,PQ,'.-', label='premier quartile pour chaque $p^0$ \n après 100 simulations')

plot(estim_ini,M,'.-', label='médiane pour chaque $p^0$ ')

plot(estim_ini,DQ,'.-', label='dernier quartile pour chaque $p^0$ ')

plot(estim_ini,C,'.-', label='centile à $97.5\%$ pour chaque $p^0$')

plt.axhline(y=0.1, label='$p*=0.1$', color='m')

plt.xlabel('estimateur initial ($p^0$)')
plt.ylabel('estimateur après la \n première itération $(p^1)$')
plt.title('$n=20$, 100 simulations')
plt.ylim(0,0.8)
legend()

plt.subplot(222)
plot(estim_ini,inf, color='r', label='intervalle de confiance de $p*$')

plot(estim_ini,sup,color='r')

plt.scatter(estim_ini,estim_itera)

plt.axhline(y=0.1, label='$p*=0.1$', color='m')

plt.xlabel('estimateur initial ($p^0$)')
plt.ylabel('estimateur après la \n première itération $(p^1)$')
plt.title('$n=20$, 1 simulation')
plt.ylim(0,0.8)
legend()

###n=1000
plt.subplot(223)

L1= [[] for j in range(len(estim_ini))]

for j in range(1,100):
    estim_iter2=[calculesti(p,tailleopt(p),1000) for p in estim_ini]
    plt.scatter(estim_ini,estim_iter2, c='black')
    for i in range (len(L)):
        L1[i].append(estim_iter2[i])

M1=[]
for i in range (0,len(L1)):
    M1.append(np.percentile(L1[i],50))

PQ1=[]
for i in range (0,len(L1)):
    PQ1.append(np.percentile(L1[i],25))

DQ1=[]
for i in range (0,len(L1)):
    DQ1.append(np.percentile(L1[i],75))

C1=[]
for i in range (0,len(L1)):
    C1.append(np.percentile(L1[i],97.5))

plot(estim_ini,PQ1,'.-', label='premier quartile pour chaque $p^0$ \n après 100 simulations')

plot(estim_ini,M1,'.-', label='médiane pour chaque $p^0$ ')

plot(estim_ini,DQ1,'.-', label='dernier quartile pour chaque $p^0$')

plot(estim_ini,C1,'.-', label='centile à $97.5\%$ pour chaque $p^0$ ')

plt.axhline(y=0.1, label='$p*=0.1$', color='m')
plt.xlabel('estimateur initial ($p^0$)')
plt.ylabel('estimateur après la \n première itération $(p^1)$')
plt.title('$n=1000$, 100 simulations')
plt.ylim(0,0.8)
legend()

plt.subplot(224)
plot(estim_ini,inf1, color='r', label='intervalle de confiance de $p*$')

plot(estim_ini,sup1,color='r')

plt.scatter(estim_ini,estim_iter1a)

plt.axhline(y=0.1, label='$p*=0.1$', color='m')

plt.xlabel('estimateur initial ($p^0$)')
plt.ylabel('estimateur après la \n première itération $(p^1)$')
plt.title('$n=1000$, 1 simulation')
plt.ylim(0,0.8)
legend()

show()



