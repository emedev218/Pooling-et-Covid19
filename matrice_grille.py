import numpy
import numpy.random
import random
n=6
L=3
p=0.04

#on donne une matrice aléatoire de taille n*n contenant des individus contaminés

#les individus suivent une loi binomiale de paramètre p
def matrice_al(n,p):
    X=numpy.random.uniform(low=0.0, high=1.0, size=(n,n))
    E=numpy.random.binomial(1, p, size=(n,n))
    Y=X * E
    return Y



def premiers(p,q):       #Teste la coprimalité de deux nombres
    while q != 0:
        p=q
        q=p%q
    pass
    return p == 1

def directions(n,L):        # Donne les L premières directions valides pour les diagonales.
    S=[]
    for i in range(1,n):
        if premiers(i,n):
            S=S+[i]
    return S[0:L]

#on calcule les charges max dans chaque pool (ie les V_l)

def test(S):                # donne le max sur une liste díndividus
    u=max(S)
    return u

def test_ligne(Y,i):        # i  entre 0 et n-1
    S=Y[i,:]
    t=test(S)
    return (t,i,"*")        #test sur la ligne i

def test_colonne(Y,i):        # i entre 0 et n-1
    S=Y[:,i]
    t=test(S)
    return (t,"*",i)        #test sur la colonne i

def diag(a,b,n):            # Sort les individus sur la diagonale de pente donnée par a,b
    S=[]
    for k in range(0,n):
        S=S+[(k,(a*k+b)%n)]
    return S

def test_diag(Y,a,b,n):
    LL=diag(a,b,n)
    S=[]
    for u in LL:
        S=S+[Y[u]]
    t=test(S)
    return (t,a,b)         #test sur la diagonale (a,b)


def serie_tests(Y,L,n):
    S=[]
    for i in range(0,n):
        T=test_ligne(Y,i)
        S=S+[T]
        pass
    for i in range(0,n):
        T=test_colonne(Y,i)
        S=S+[T]
        pass
    for a in directions(n,L-2):
        for b in range(0,n):
            T=test_diag(Y,a,b,n)
            S=S+[T]
            pass
        pass
    return S


def in_test(i,j,T,n):
    (t,a,b)=T
    if (a=="*" and b==j):
        u=True
    elif (a==i and b=="*"):
        u=True
    else:
        if (a=="*" or b=="*"):
            u=False
        else:
            u=((i,j) in diag(a,b,n))
    return u

def collec_tests(i,j,S,n):
    SS=[]
    for T in S:
        if in_test(i,j,T,n):
            SS=SS+[T]
    return SS


def niv_contam(Y,L,n):
    S=serie_tests(Y,L,n)
    W=Y*0
    for i in range(0,n):
        for j in range(0,n):
            SS=collec_tests(i,j,S,n)
            C=[]
            for s in SS:
                C=C+[s[0]]
            c=min(C)
            P=C.count(c)>=2
            W[i,j]=P*c
        pass
    pass
    return W

def conta(Y,L,n):  #on crée la matrice R, qui donnera l'information sur les contaminés
    W=niv_contam(Y,L,n)
    R=np.zeros((n,n))
    for i in range(0,n):
        for j in range(0,n):
            if W[i][j]>0:
                R[i][j]=1
    return R

def ident(Y,L,n):
    R=conta(Y,L,n)
    C=[]
    for i in range(0,n):
        for j in range(0,n):
            if R[i][j]==1:
                C.append((i+1,j+1))
    return C

Y=matrice_al(n,p)
S=serie_tests(Y,L,n)
W=niv_contam(Y,L,n)
R=conta(Y,L,n)



print("Les paramètres sont ", "p=",p, "n=",n,"( N=n^2=",n**2,")",  "L=",L)
print("La matrice initiale \n",Y,"\n\n","================================")
print("La matrice donnée par l'algorithme\n",R,"\n\n","================================")
if ident(Y,L,n) !=[]:
    print("ce qui signifie que le(s) prélèvements infecté(s) correspond(ent) aux coordonnées", ident(Y,L,n))
else:
    print("ce qui signifie qu'il n'y aucun prélèvement infecté")
 
