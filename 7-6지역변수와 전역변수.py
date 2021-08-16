# 지역변수는 함수 내에서만 쓸 수 있는 것, 함수 호출이 끝나면 사라지는 것.
# 전역변수는 프로그램 내에서 어디서든지 부를 수 있는 함수.

gun = 10

def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun 사용 #밖에꺼 쓴다고
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무
print("남은 총 : {0}".format(gun))


#전역 변수 많이 쓰면 코드 관리 어려워짐.... 가급적 권장하는 방법은 아님

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun













