class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
        
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)


#  # __init__  : 파이썬에서 쓰이는 생성자. 마린, 탱크.. 객체가 만들어질떄
 #자동으로 호출되는. 
 #객체. - 클래스로부터 만들어지는 녀석들을 객체라고 표현. 
 #마린과 탱크는 Unit 클래스의 init... self 제외하고 동일한 값을 던져줘야함.






