from encode import *
from decode import *

print("-->please enter length of Code (n)")
n=int(input())
print("-->please enter dimension of Code (k)")
k=int(input())
C=generateCode(n,k)
minC=C.minimum_distance()
print("-->please enter the message you want encoded")
msg=input()
msgBin=encodeToBinary(msg)
msgBin,length=binaryAdapter(msgBin,k)
print("\n\n")
print("-->Generator matrix for code")
print(C.generator_matrix())
print("\n\n")
print("--Minimum distance for code")
print(minC)
print("\n\n")
encodedMessage=encode(msgBin,k,C)
print("\n\n")
decoded=decode(C,encodedMessage,length,n)
print("\n\n")
decodeToString(decoded)