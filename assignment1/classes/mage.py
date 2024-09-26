import random
from .base import CharacterBase

class Mage(CharacterBase):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        self.intelligence = 10

    def attack(self):
        print("Вы атаковали магией")
        return self.intelligence * 2
    
    def cast_ability(self):
        print("Вы использовали мощное заклинание")
        damage = self.intelligence + random.randint(self.intelligence//2, self.intelligence*2)
        self.mana -=5
        return damage

    def _defence(self, piercing):
        return piercing(self.intelligence // 2)