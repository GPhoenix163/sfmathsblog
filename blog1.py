# This is the code associated with blog post #1 on https://sfmaths.home.blog

from pyfinite import ffield
import numpy
import random

alphabet1 = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

class LatinSquare:
    
    def __init__(self,n=3,u=1,alphabet=alphabet1):
        self.n = 3
        self.Field = ffield.FField(n) #Galois Field GF(2^n)
        self.array = [[alphabet[self.Field.Add(self.Field.Multiply(u,i),2**n-1-j)] for j in range(2**n)] for i in range(2**n)]

    def __call__(self,i,j):
        return self.array[i][j]

    def __str__(self):
        return str(numpy.matrix(self.array))

class LSCode:

    def __init__(self,bits=4,char_pow=2,given_code=None,alphabet=alphabet1):
        if given_code == None:
            if 2**char_pow-1 < bits-2:
                raise
            self.orthogonalLatinSquares = [LatinSquare(char_pow,i,alphabet) for i in range(1,bits-1)]
            self.code = []
            for i in range(2**char_pow):
                for j in range(2**char_pow):
                    lsc = [self.orthogonalLatinSquares[k](i,j) for k in range(len(self.orthogonalLatinSquares))]
                    lscs = ""
                    for m in range(len(lsc)):
                        lscs += str(lsc[m])
                    self.code.append(str(alphabet[i])+str(alphabet[j])+lscs)
        else:
            self.code = given_code

    def __str__(self):
        return str(self.code)

    def __mul__(self,other):
        cdata = []
        for i in range(len(self.code)):
            cdata += [self.code[i]+other.code[j] for j in range(len(other.code))]
        return LSCode(given_code=cdata)

    def __call__(self,i):
        return self.code[i]    

def hamming(x,y):
    d = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            d += 1
    return d

def md(code):
    m = len(code.code[0])
    for i in range(len(code.code)):
        for j in range(i+1,len(code.code)):
            if hamming(code.code[i],code.code[j]) < m:
                m = hamming(code.code[i],code.code[j])
                print(m,code.code[i],code.code[j])
    return m
