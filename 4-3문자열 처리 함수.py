python = "Python is Amazing"
print(python.lower()) #lower는 소문자로.
print(python.upper()) #upper는 대문자로.

print(python[0]. isupper()) #파이썬 0번째가 대문자인지 소문자인지 True
print(len(python)) #len은 글자 수.

print(python.replace("Python", "Jave")) #replace 바꾸기

index = python.index("n") #색인. 찾기. indwx
print(index) #몇번째에 위치하는가.

index = python.index("n", index + 1) #하나를 더한. 또 n이 나오는 위치. 
print(index) # 두번째 n은 15위치. 

print(python. find("Jave")) # -1이 뜸. 내가 원하는 값이 이 변수에 포함되지 않다는 뜻임.
#print(python.index("Jave")) # 오류 뜸. 파이썬이라는 변수에는 자바가 없기 때문에 에러를 내는거임.
#find에서는 원하는 값이 없을 때는 -1. index 오류남.
print("hi")

print(python.count("n")) #이 변수에서 n이 몇 번 등장하느냐.




