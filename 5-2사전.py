# 키는 키에 해당하는 사물함을 열 수 있는... 키는 중복이 안됨.
#  100번을 받았는데 다른 사람이 100번 받으면 안되는거고...


# cabinet = {3: "유재석", 100: "김태호"}
# # print(cabinet[3] + cabinet[100])
# # print(cabinet[100])

# # print(cabinet.get(3))
# # print(cabinet[5])
# print(cabinet.get(5))
# print(cabinet.get(5, "사용 가능")) # None......
# print("hi")

# print(3 in cabinet) # 3이라는 변수가 캐비넷에 있으면 True
# print(5 in cabinet)

cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호" 
print(cabinet)

# 손님이 갔어
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)






