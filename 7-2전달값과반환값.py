# 함수는 어떤 역할을 하는 박스..... def
# 함수는 정의만 해두는거지 호출하기 전까지는..
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): #deposit이라는 입금...
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance+money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money:
        print("출금이 완료ㅕ되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금 완료 아님. 잔액은 {0}원입니다.".format(balance))
        return balance

def withdraw_night(balnace, money): #저녁에 출금
    commission = 100 #수수료 100원
    return commission, balance - money - commission

balance = 0 # 잔액
balance = deposit(balance, 1000)

commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))


###################################################################################