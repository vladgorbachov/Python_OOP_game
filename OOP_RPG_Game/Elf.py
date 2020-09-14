from Beginner import Beginner
import random
from random import random

class Elf(Beginner):

    def __init__(self, username):
        super().__init__(username)
        self.SetPwr(5)
        self.SetInt(5)
        self.SetEng(5)
        self.SetHp(self.GetHp() + self.GetPwr())

    def extendedAttack(self, character):
        chance = randint(1, 100)
        if chance <= 10:
            print('Fault')
        elif chance >= 95:
            self.new_damage = self.GetDamage() + random.randint(0, self.GetInt()) + (self.GetDamage() + random.randint(0, self.GetInt()) * .5)
            character.ReduceHp(self.new_damage)
            print(f'{self.GetUserName()} making extended attack! -{self.new_damage}')

        else:
            self.new_damage = self.GetDamage() + random.randint(0, self.GetInt())
            character.ReduceHp(self.new_damage)
            print(f'{self.GetUserName()} making extended attack! -{self.new_damage}')

    def inactive(self):
        self.SetInt(self.GetInt() + 2)
        print(f'{self.GetUserName()} increased him intellect up to {self.GetInt()}')
