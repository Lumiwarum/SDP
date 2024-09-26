from .base import CharacterBase

class Knight(CharacterBase):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        self.strength = 10
        self.stand = False

    def attack(self):
        damage = self.strength
        if self.stand:
            self.stand = False
            self.strength -=10
        return damage
    
    def cast_ability(self):
        if self.stand:
            print("Уже в стойке, наносим обучную атаку")
            return self.attack()
        self.strength += 10
        self.mana -= 10
        self.stand = True
        return 0

    def _defence(self):
        return self.strength
    
if __name__ == "__main__":
    print("aa")