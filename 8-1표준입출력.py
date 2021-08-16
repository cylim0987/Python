# print("Python", "Javaa", sep=" , ", end="ㅗ")
# print("무엇이 더 재밌을까요?") 
# # sep 사이에 넣는 것.
# # end 는 문장의 끝부분을 ?(물음표)로 바꿔달라...

# import sys
# print("Python", "Javaa", file=sys.stdout)
# print("Python", "Javaa", file=sys.stderr)


# stdout 표준 출력 . stderr 표준 에러로 처리



# # 시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#      print(subject.ljust(8), str(score).rjust(4), sep=":") 
#      #ljust(숫자) 여럳ㅂ개의 공간. # rjust(숫자) 오른쪽 정렬 4칸 공간확보

# # 은행 대기 순번표
# # 001 002 003 ....
# for number in range(1, 21):
#     print("대기번호 : " + str(number).zfill(3)) #zfill 3개만큼의 크기 공간확보
    

# answer = input("아무 값이나 입력하세요 : ")
answer = 10
print(type(answer))
# print("입력하신 값은 " + answer + "입니다.") #숫자만 하려면 str?











