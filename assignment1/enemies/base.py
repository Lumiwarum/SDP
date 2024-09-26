from abc import ABC, abstractmethod
import numpy as np

class MonsterBase(ABC):
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.health = 100
        self.rage = 0

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def _defence(self):
        return 0

    def _take_damage(self, damage):
        taken_dmg = np.max([(damage-self._defence()),0])
        self.health -= taken_dmg
        print(f"{self.name} получил {taken_dmg} урона\nОсталось {self.health} здоровья")
        if self.health <= 0:
            print(f"{self.name} умер!")
            return True
        return False