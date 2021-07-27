from re import L
from sage.all import *
import binascii


def decode(CODE,msg,length,n):
    enList=list(msg)
    numC=[]
    D=CODE.decoder()
    for i in enList:
        numC.append(int(i))
    decMsg=[]
    for i in range(0,len(numC),n):
        part=[]
        r=vector(GF(2),numC[i:i+n])
        part=D.decode_to_message(r)
        for i in part:
            decMsg.append(i)

    decMsgStr=""
    counter=0
    for i in decMsg:
        if(counter>=length):
            break
        else:
            decMsgStr+=str(i)
            counter+=1
    print("-->Decoded Message:")
    print(decMsgStr)
    return decMsgStr


#CONVERTS BINARY TO STRING OF ASCII CHARACTERS
def decodeToString(msg):
    msgList=list(msg)
    letters=[]
    for i in range(0,len(msgList),8):
        letter=msgList[i:i+8]
        l=''.join(letter)
        letters.append(chr(int(l,2)))
    print("-->Decoded message in characters is:")
    print(''.join(letters))
    return ''.join(letters)