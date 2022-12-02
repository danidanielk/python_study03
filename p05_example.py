'''
Created on 2022. 11. 9.

@author: NT731QCJ-K582D
'''
# up / down 게임 (함수)
# 유저의 이름을 입력받고 환영하는 인사를 출력
# 컴퓨터 1~100 사이의 랜덤한 숫자를 하나 뽑아서
# 유저에게 정답을 입력하게 했을 때
# 저 범위의 숫자가 아니면 다시 입력하도록
# 입력한 숫자가 정답보다 작으면 "up"
# 입력한 숫자가 정답보다 크다면 "Down"출력
# 정답을 맞췄을 때는 몇번만에 맞췄는지 출력 + 종료
# 기회는 10 회로 제한.
import random

def user ():
    name= input("name ")
    print(name)


def getComAns():
    comAns= random.randint(1, 100)
    return comAns
    

def explainRule():
    print("맞춰바")


def sayUserAnser():
    userAns=int(input("입력 : "))
    if (userAns > 100) or userAns<0:
        print("1~100 사이로 입력해주세요")
        sayUserAnser()
    return userAns


user()
comAns=getComAns()
explainRule()

count=0
userAns =0

while count < 10:
    userAns=sayUserAnser()
    count +1
    
    if count >10:
        print("lose 게임종료")
    if userAns < comAns:
        print("up")
    elif userAns > comAns:
        print("down")
    else:
        print("정답.")
        break