# # 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students] # i에다가 100을 더한 값을 넣을건데 이 i는
# # student라는 리스트에 있는 값을 불러오면서 뭐?
# print(students)

# # 학생들 이름을 길이로 변환
# students = ["iron man", "thor", "i am groot"]
# students = [len(i) for i in students] # 글자 수.
# print(students)


# 학새 이름을 대문자로 변환
students = ["IRON MAN", "THOR", "I AM GROOT"]
students = [i.lower() for i in students]
print(students)







