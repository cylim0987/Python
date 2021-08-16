# 리스트 : 순서를 가지는 객체의 집합. 
# 지하철을 타는데 지하철 칸별로 10명, 20명, 30명이 있다고 가정.

subway1 = 10
subway2 = 20
subway3 = 30 # 이것들을 하나로 연속적인 공간에 묶음

subway = [10, 20, 30]
print(subway)


subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번재 칸에 타고 있는가?
print(subway.index("조세호")) #인덱스는 0번째, 1번째 니까 조세호는 1번째임.

# 하하씨가 다음 정류장에서 다음 칸에 탐.

subway.append("하하") # append는 더하는 것.
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄

subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄

print(subway.pop()) # pop 뒤에서부터 꺼내는 것.
print(subway)

# print(subway.pop()) # pop 뒤에서부터 꺼내는 것.
# print(subway)

# print(subway.pop()) # pop 뒤에서부터 꺼내는 것.
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인하기

subway.append("유재석")
print(subway)
print(subway.count("유재석")) #유재석이 2명이 있었다고 나옴.

# 정렬도 가능

num_list = [5, 2, 3, 2, 1]
num_list.sort() # sort는 정리한다는 뜻.
print(num_list)

# 순서 뒤집기도 가능

num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용

num_list = [5, 2, 3, 2, 1]
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)











