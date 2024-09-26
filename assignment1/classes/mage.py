import random
from .base import CharacterBase

class Mage(CharacterBase):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        self.intelligence = 10

    def attack(self):
        print("Вы атаковали магией")
        self.mana +=10
        return self.intelligence * 2
    
    def cast_ability(self):
        if self.mana <30:
            print("Не хватает маны")
            return self.attack()
        print("Вы использовали мощное заклинание")
        damage = self.intelligence + random.randint(self.intelligence//2, self.intelligence*3)
        self.mana -=30
        return damage

    def _defence(self, piercing):
        return piercing(self.intelligence // 2)