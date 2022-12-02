'''
Created on 2022. 11. 9.

@author: NT731QCJ-K582D
'''
import random

#가위바위보 질때까지 ,몇번이겼는지

def user ():
    print("1 - 가위")
    print("2 - 바위")
    print("3 - 보")
    a= int(input("숫자를 입력하세요."))
    if a == None or (0 >= a >3):
        print("잘못 입력하셨습니다.")
        user()
    return a

def com():
    b=random.randint(1, 3)
    return b

def play(userA,comB):
    while True:
        count=0
        userA=user()   
        comB=com()
        if (userA==1 and comB==1) or (userA==2 and comB==2) or (userA==3 and comB==3):
            print("무승부")
            
        elif(userA==1 and comB==3) or (userA==2 and comB==1) or (userA==3 and comB==2):
            print("승리")
            count+=1
            
        else:
            print("패")
            print(count,"승")
            break

userA=user()
comB=com()
play(userA, comB)
    