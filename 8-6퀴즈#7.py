# 매주 1회 작성해야 하는 보고서

# - X 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램 작성

# 조건 : 파일명은 '1주차,txt', '2주차.txt', ......


# -*- coding: utf-8 -*-
for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding = "utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 - \n".format(i))
        report_file.write("부서 : \n")
        report_file.write("이름 : \n")
        report_file.write("업무 요약 : \n")



