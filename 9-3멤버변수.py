class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
        
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# . 클래스 내에서 정의 된 변수 self.hp,name 등


# 레이스 : 공중 유닛, 비행기, 클로킹 기능(투명)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

#상대방이 프로토스. 마인드 컨트롤..
# 마컨 : 상대방 유닛을 내 것으로.
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# 객체 추가 변수 외부로........ 
# wraith1은 클로킹이 없어서 넣으면 오류.


