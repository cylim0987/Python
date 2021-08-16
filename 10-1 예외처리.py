# 주소는 11층인데 막상 아ㅏ트는 10층이라던지.. 잔액 없는.. 에러상황
# 계산기 숫자입력받아 문자입력을
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요.")))
    nums.append(int(input("두 번째 숫자를 입/하세요.")))
    #nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값이다.")

# ZeroDivisionError: division by zero

except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러발생")
    print(err)






