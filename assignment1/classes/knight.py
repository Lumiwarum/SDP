from .base import CharacterBase

class Knight(CharacterBase):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        self.strength = 10
        self.stand = False
        self.mana = 40

    def attack(self):
        damage = self.strength
        self.mana +=5
        if self.stand:
            self.stand = False
            self.strength -=10
        return damage
    
    def cast_ability(self):
        if self.mana <=15:
            print("Не хватает маны, наношу обучную атаку")
            return self.attack()
        if self.stand:
            print("Уже в стойке, наносим обучную атаку")
            return self.attack()
        print("Вы вошли в стойку")
        self.strength += 10
        self.mana -= 15
        self.stand = True
        return 0

    def _defence(self, piercing):
        if self.mana> 5 and self.stand:
            print("Защита через сильный блок")
            self.mana -=5
            return piercing(self.strength+5* self.level)
        return piercing(self.strength)