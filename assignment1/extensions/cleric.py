from .base import CharacterBase

class Cleric(CharacterBase):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        self.strength = 10
        self.mana = 30

    def attack(self):
        damage = self.strength
        self.mana +=5
        return damage
    
    def cast_ability(self):
        if self.mana <=10:
            print("Не хватает маны, наношу обучную атаку")
            return self.attack()
        print("Вы исцелились")
        self.mana -= 10
        self.health += 20
        self.stand = True
        return 0

    def _defence(self, piercing):
        return piercing(self.strength)