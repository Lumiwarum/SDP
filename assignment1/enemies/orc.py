from .base import MonsterBase
class Orc(MonsterBase):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        self.strength = 8 * self.level
        self.health = 130

    def attack(self):
        if self.rage >1:
            damage = self.strength + self.strength // 2
        else:
            damage = self.strength
        self.rage = (self.rage+1)%5
        return damage

    def _defence(self):
        return self.strength if self.rage <2 else 0