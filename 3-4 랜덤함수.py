# #랜덤함수는 난수
from random import * # * 들어가야됨?

print(random()) #랜덤으로 막 뜸. 근데 왜  0.???로 그냥 랜덤이라서 난수? 0.0 이상 ~ 1.0 미만의 임의의 값 생성하는 의미.
print(random() * 10) # 0.0~ 10.0 미만의 임의의 값 생성. 여기서 0.0*니까 0.0이 나올수도 있나?
print(int(random() *10)) #0~ 10 미만의 임의의 값 생성. int는 정수.
print(int(random() *10))
print(int(random() *10))
print(int(random() *10)) 

#로또 숫자 뽑기?
print(int(random() * 10) + 1) # 1~ 10 이하의 임의의 값.
print(int(random() * 10) + 1)
print(int(random() * 10) + 1)
print(int(random() * 10) + 1)
print(int(random() * 10) + 1)

print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1) 
# 44 +1이 아니라 45+1이다. 왜냐면 0부터 시작이니까

print(randrange(1, 46)) # 1~45는 1~ 45 미만의 값 생성이니까. 46까지로 해야함.
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))


print(randint(1, 45)) #1부터 45 이하의 임의의 값 생성.
# *6
