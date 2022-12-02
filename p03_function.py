'''
Created on 2022. 11. 9.

@author: NT731QCJ-K582D
'''

#function(함수)
# def 함수명(파라미터명):
#    code

def test():
    print("배불러") 
test()

#함수 아직 미완성 시 패스라도 써서 매꿔
def test2():
    pass



a=int(input("입력 "))
b=int(input("입력 "))
 
def plus(a,b):
    c=a+b
    print(c)
plus(a, b)



#정수 2개 넣으면 사칙연산 구하는 함수
def calc(a,b):
    '''
    설명서
    이 설명서는 어쩌고저쩌고
    '''
    
    q=a+b
    w=a-b
    e=a*b
    r=a/b
    return q,w,e,r #튜플상태 하나 리턴.
d=calc(20,10)
print(d)
u,i,o,p=calc(20,10)
print(u,i,o,p)
uu,ii,_,pp=calc(20,10) #_ 아래하이픈 처리하면 안가져올수있음
print(uu,ii,pp)