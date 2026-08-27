class Hero:
    def __init__(self, name, HP):
        self.name = name
        self.HP = HP
    def take_damage(self, amount1):
        self.HP -= amount1
        if amount1 == 0:
            amount2 = "no"
        else:
            amount2 = amount1
        print(self.name,"took",amount2,"damage!")
        print(self.name,"has",self.HP,"/",self.HP+amount1,"HP left.")

hero1 = Hero("Arthur", 100)
hero1.take_damage (10)
hero2 = Hero("Morgana", 100)
hero2.take_damage (0)
