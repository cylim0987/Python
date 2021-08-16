#

# http://naver.com

# 규칙 1 : 슬라이싱 이용..
# 규칙 2 : 이것도 슬라이싱 이용.
# # 규칙 3은. 이것도 슬라이싱인가?글자 내 e 갯수

# eeee = "http://naver.com"
# print(len(eeee))
# print(eeee.count("e"))

# print("생성된 비밀번호 : " + eeee[7: 10] + len(eeee))


#정답

url = "http://naver.com"
my_str = url.replace("http://", "") # 앞에꺼를 뒤에껄로 바꿈 # 규칙1
# print(my_str)
my_str = my_str[:my_str.index(".")] 
# 규칙 2. my_str[0:5] -> 0~5 직전까지. 변수 문자열 중에서 처음 나오는 .점의 위치 직전까지. 0
# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다. ".format(url, password))

#