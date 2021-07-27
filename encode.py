from sage.all import *
import random

def generateCode(n,k):
    g=[]
    col=[]
    #CREATION OF GENERATION MATRIX
    for i in range(0,k):
        for j in range(0,k):
            if(i==j):
                col.append(1)
            else:
                col.append(0)
        g.append(col)
        col=[]
    for i in range(0,k):
        for j in range(0,n-k):
            g[i].append(random.randint(0,1))
    G=matrix(GF(2),g)
    C=codes.LinearCode(G)
    return C

def encodeToBinary(msg):
    m=list(msg)
    mNumbers=[]
    for i in m:
        mNumbers.append(ord(i))
    mBin=[]
    for i in mNumbers:
        l=bin(i)
        l=l[2:]
        l="00000000"+l
        mBin.append(l[-8:])
    #print(m)
    #print(mNumbers)
    #print(mBin)
    mBin="".join(mBin)
    print("-->Message in pure binary form\t"+str(mBin))
    return mBin

#ADDS ENOUGH ZEROES TO EVEN OUT THE PIECES OF THE CONVERSION
def binaryAdapter(c,k):
    original=len(c)
    if(len(c)%k==0):
        return c,len(c)
    else:
        while(len(c)%k!=0):
            c+="0"
    return c,original

#ENCODE THE MESSAGE THROUGH THE LINEAR CODE
def encode(c,k,CODE):
    newMsg=[]
    for i in range(0,len(c),k):
        part=[]
        v=vector(GF(2),c[i:i+k])
        part=CODE.encode(v)
        for i in part:
            newMsg.append(i)
    msg=""
    for i in newMsg:
        msg+=str(i)
    print("-->Encoded message is")
    print(msg)
    return msg


    

    