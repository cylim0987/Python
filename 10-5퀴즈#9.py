# 대기손님.... 자동 주문 시스템 제작.
# 조건 1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueERROR로 찍어라.
# 조건 2: 대기소문 주문 총량은 10마리. 
# 치킨 소진시 SOLDOUTERROR주문 발생ㅅ키고 재고가 소진되어.


class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1
while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다." \
                .format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError    
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문 안 받음.")
        break # while문 탈출.



            