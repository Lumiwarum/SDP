import random
from .base import CharacterBase

class Mage(CharacterBase):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        self.intelligence = 10

    def attack(self):
        return self.intelligence * 2
    
    def cast_ability(self):
        damage = self.intelligence + random.randint(self.intelligence//2, self.intelligence*2)
        self.mana -=5
        return damage

    def _defence(self):
        return self.intelligence // 2