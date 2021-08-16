# 모듈은 필요한 것들끼리 부품으로 이루어진 파일.
# 범퍼만 파손되면 범퍼만 교체하면 되는... 소프트웨어도 부품만 교체하거나 추가
# 유지보수가 쉬움. 


# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 떄 가격
# theater_module.price_morning(4) # 4명이서
# theater_module.price_soldier(5) 




# import theater_module as mv # as 뒤에 뭔가 붙이기. 용량 줄이기.
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)


# from theater_module import *
# # from random import * 이랑 똑같은거
# # price(3)
# # price_morning(4)
# # price_soldier(5)

# from theater_module import price, price_morning #필요한 함수만... p
# price(5)
# price_morning(6)
# # price_soldier(4)

from theater_module import price_soldier as price
price(5)






