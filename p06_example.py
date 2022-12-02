'''
Created on 2022. 11. 9.

@author: NT731QCJ-K582D
'''
import random
from random import randint


#가위바위보 한번 질 때 까지, 총 몇번 이겼는지 출력

handTable = [None,"가위","바위","보"]

def printRule():
    for i, h in enumerate(handTable):
        if (i !=0):
            print("[%d] %s" %(i,h))
    print("------")        

def comFire():
    return randint(1,3)

def userFire():
    print("------")
    uh=int(input("입력: "))
    if(1<=uh<=3):
        return uh
    return userFire()

def printHand(uhuh,chch):
    print("유저:%s" %handTable[uhuh])
    print("컴터:%s" %handTable[chch])
    
def judge(uhuh,chch):
    t= uhuh-chch
    if t==0:
        print("무승부")
        return 0
    elif t== -1 or t==2:
        print("패")
        return 999
    else:
        print("승")
        return 1
    
def playGame(uHand,cHand, result, winCount):
    while True:
        uHand=userFire()
        cHand=comFire()
        printHand(uHand, cHand)
        result=judge(uHand,cHand)
        if result == 999:
            print("종료")
            break
        winCount += result
    print(winCount,"승으로 종료")
        
printRule()
uHand, cHand, result, winCount=0,0,0,0
playGame(uHand, cHand, result, winCount)
