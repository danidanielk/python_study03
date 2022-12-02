'''
Created on 2022. 11. 9.

@author: NT731QCJ-K582D
'''

l=[123,45,6,78,910]
for ll in l:
    print(ll, sep=" " )
    
    
for eee in range(10):
    print("z")
    print(eee)
    
for w in range(1,21,2):
    print(w)
    
    
while True:
    y=int(input("Y: "))
    if y % 2==0:
        print("짝수")
        break
    
    
#enumerate : 반복문 사용할때 반복문이 몇번 반복되었는지 확인필요할때 사용.
#            (인덱스,값) 튜플 형태로 리턴이 된다.

ll=[33,44,55,66,77]
for i,v in enumerate(ll):
    print(i+1,v)
    
#1등 학생을 몇번째에  ? 점수는 몇점인지 출력
maxi, maxS = 0,0 #튜플형태
for i,v in enumerate(ll):
    if maxS <v:
        maxS=v
        maxi=i
print(maxi,maxS)
    
