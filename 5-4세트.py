# 세트 (set) . 집합. 중복 안됨, 순서 없음

my_set = {1,2,3,3,3} #중복 안됨
print(my_set)

java = {"유재석", "김태호", "박명수"}
python = set(["유재석", "이광수"])

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)

print(java & python) # 유재석이 나옴

print(java.intersection(python)) # 똑같이 교집합

# 합집합(java도 할 수 있거나 python을 할 수 있는 개발자) 둘 중에 하나만 해도.

print(java | python) # | 는 or
print(java.union(python))   #순서 보장 x

# 차집합 자바는 할 줄 알지만 파이썬을 할줄 모르느 사람들에게 교육을 하겠
# 다...라면.

print(java - python)
print(java. difference(python))


# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)


# java를 까먹음
java.remove("김태호")
print(java)




