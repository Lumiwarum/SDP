from abc import ABC, abstractmethod
import numpy as np

class CharacterBase(ABC):
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.health = 100
        self.mana = 100

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def cast_ability(self):
        pass

    @abstractmethod
    def _defence(self):
        return 0

    def take_damage(self, damage):
        self.health -= np.max([(damage-self._defence()),0])
        if self.health <= 0:
            print(f"{self.name} умер!")
            return True
        return False
