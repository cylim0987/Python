# 튜플은 리스트와는 다르게 내용변경과 추가를 할 수 없음. 
# 속도가 리스트보다 빠름

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") #오류 남.

# 튜플은 어디서 선호되는..

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)







