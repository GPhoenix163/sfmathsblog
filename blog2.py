# Python Code Associated with blog post #2 at https://sfmaths.home.blog

def fact(n):
    p = 1
    for i in range(2,n+1):
        p *= i
    return p

def floor(x):
    return int(x)

def ceil(x):
    return int(x)+1

def binom(n,k):
    return (fact(n)) // (fact(k)*fact(n-k))

def Singleton(n,d=3,q=4):
    return q**(n-d+1)

def Hamming(n,d=3,q=4):
    return (q**n) / sum(binom(n,i)*(q-1)**i for i in range(floor(0.5*(d-1))+1))

def GilbVasha(n,d=3,q=4):
    return (q**n) / sum(binom(n,i)*(q-1)**i for i in range(d))

def printout(d,q,ite=10):
    for i in range(d+1,d+1+ite):
        print("n="+str(i),"Singleton: "+str(Singleton(i,d,q)),"Hamming: "+str(floor(Hamming(i,d,q))),"Gilbert-Vashamov: "+str(ceil(GilbVasha(i,d,q))))

def getrange(n,d,q):
    return print("The maximal "+str(n)+"-code with minimum distance "+str(d)+" over "+str(q)+" characters has cardinality between "+str(ceil(GilbVasha(n,d,q)))+" and "+str(min(Singleton(n,d,q),floor(Hamming(n,d,q)))))


# Added in for a bit of fun, used in some code that was later deleted.

from math import log

def hamming(x,y):
    d = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            d += 1
    return d

def toBaseQ(n,q,l = 0):
    k = int(log(n,q))
    string = ""
    for i in range(k+1):
        if q**(k-i) <= n:
            for m in range(1,q):
                if (q-m)*q**(k-i) <= n:
                    string += str(q-m)
                    n -= (q-m)*q**(k-i)
                    break
        else:
            string += "0"
    if l > 0:
        r = l - len(string)
        if r > 0:
            for j in range(r):
                string = "0"+string
    return string
        
