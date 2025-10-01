class GameCharacter:
    level=1
    experience=0
    def __init__(self,agender,age):
        self.agender=agender
        self.age=age
    def 跃起(self):
        print("什么也没有发生")
class 战士(GameCharacter): #继承GameCharacter的所有属性
    def attack(self):
        print(f"{self.agender}使用了冲撞")
p1=GameCharacter("female",11) #创建角色
p2=GameCharacter("male",18)
p1.name="hunter" #命名
p2.name="cheater"
p3=战士("male",24)
print(p3.attack())






