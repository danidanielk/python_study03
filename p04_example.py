'''
Created on 2022. 11. 9.

@author: NT731QCJ-K582D
'''
import random

i=random.randint(1, 10)
print(i)


#로또번호 6개 중복없이 출력

def lotto():
    return random.randint(1, 45)
numlist=[]
count=0

while count < 6:
    num=lotto()
    if num not in numlist:
        numlist.append(num)
        count +=1
        
for n in numlist:
    print(n,end=" ") 
    
    
    
print()
    
    
    
    
def lo ():
    return random.randint(1, 45)
l = []
countt=0

while countt <6:
    a = lo()
    if a not in l:
        l.append(a)
        countt+=1
        
for i in l:
    print(i,end=" ")
    