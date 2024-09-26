from .base import MonsterBase
import random

class Skeleton(MonsterBase):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        self.agility = 7 * self.level
        self.high_ground = False
        self.health = 70

    def attack(self):
        if self.rage >1:
            self.rage = 0
            pierce = lambda x: int(x * 0.7)
            return self._back_charge(), pierce
        damage = self.agility
        self.rage +=1
        return damage, lambda x: x
    
    def _back_charge(self):
        self.high_ground = True
        return self.agility+random.randint(1, self.agility//2)

    def _defence(self):
        return 90 if self.high_ground else self.agility