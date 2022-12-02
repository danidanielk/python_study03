'''
Created on 2022. 11. 9.

@author: NT731QCJ-K582D
'''

#점수 큰거부터..
score=int(input ("점수"))
if (score >=80):
    print("A")
elif (score >=70):
    print("B")
elif (score >= 60):
    print("C")
else:
    print("D")

#in ,not in
a = {"name":"다니", "age":19, "phone":"010-1111-2222"}
print("name" in a)
print(20 in a.values()) # a딕트에 20이라는 벨류가 있니
print("height" not in a)