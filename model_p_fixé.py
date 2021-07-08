from math import *
from matplotlib.pyplot import plot, show, legend

def fonction(p, n): 
    x = np.arange(1, n)
    y = (2*(1-p)/(x*0.005)*np.sqrt((1-(1-p)**x)/(1-p)**x))**2
    yp = x*y
    return(x, y, yp)

x, y, yp = fonction(p=0.01, n=600)
x1, y1, y1p = fonction(p=0.03, n=175)
x2, y2, y2p = fonction(p=0.05, n=100)
x3, y3, y3p = fonction(p=0.15, n=25)

fig = plt.figure(figsize=(16,16))
fig.subplots_adjust(hspace=0.4, wspace=0.4)

# fig 1
i = 1
axe11_X = fig.add_subplot(2, 2, i)
axe12_X = axe11_X.twinx()
axe11_X.plot(x, y, 'r-')
axe12_X.plot(x, yp, 'b-')
axe11_X.set_xlabel('taille des pools ($N$)')
axe11_X.set_ylabel('nombre de tests ($n$)', color='r')
axe12_X.set_ylabel('nombre total de prélèvements ($nN$)', color='b')
plt.title('$p=1\%$')

#fig 2
i = 2
axe21_X = fig.add_subplot(2, 2, i)
axe22_X = axe21_X.twinx()
axe21_X.plot(x1, y1, 'r-')
axe22_X.plot(x1, y1p, 'b-')
axe21_X.set_xlabel('taille des pools ($N$)')
axe21_X.set_ylabel('nombre de tests ($n$)', color='r')
axe22_X.set_ylabel('Y1p data', color='b')
plt.title('$p=3\%$')

#fig 3
i = 3
axe31_X = fig.add_subplot(2, 2, i)
axe32_X = axe31_X.twinx()
axe31_X.plot(x2, y2, 'r-')
axe32_X.plot(x2, y2p, 'b-')
axe31_X.set_xlabel('taille des pools ($N$)')
axe31_X.set_ylabel('nombre de tests ($n$)', color='r')
axe32_X.set_ylabel('nombre total de prélèvements ($nN$)', color='b')

plt.title('$p=5\%$')
#fig 4
i = 4
axe41_X = fig.add_subplot(2, 2, i)
axe42_X = axe41_X.twinx()
axe41_X.plot(x3, y3, 'r-')
axe42_X.plot(x3, y3p, 'b-')
axe41_X.set_xlabel('taille des pools ($N$)')
axe41_X.set_ylabel('nombre de tests ($n$)', color='r')
axe42_X.set_ylabel('nombre total de prélèvements ($nN$)', color='b')
plt.title('$p=15\%$')

show()
