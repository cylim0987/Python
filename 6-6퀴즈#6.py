# # 50명... 탑승 수를 구하는 프로그램

# 조건 1 : 5분~ 50분 사이의 난수..
# 조건 2 : 5분ㄴ~ 15분 사이만 매칭해야됨.
# # # 하루에 50명의 승객이 매칭할거임.

# xkqtmdror = range(1, 51)
# for xkqtmdror in range(1, 51)
# print(xkqtmdror)

from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): # 1 ~ 50 승객 수.
    time = randrange(5, 51) # 5분 ~ 50분 소요 시간
    if 5<= time <= 15: # 5분 ~ 15분 이내의 손님, 탑승 승객 수 증가 처리
        print("[0] {0}번째 손님 (소요시간 : {1}분".format(i, time))
        cnt += 1
    else: # 매칭 실패한 경우
        print("[ ] {0}번째 손님(소요시간 : {1}분".format(i, time))

print("총 탑승 승객 수 : {0} 분".format(cnt))

