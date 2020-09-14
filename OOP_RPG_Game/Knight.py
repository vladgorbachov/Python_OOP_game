from Beginner import Beginner
from random import randint


class Knight(Beginner):


    def __init__(self, username):
        super().__init__(username)
        self.SetPwr(5)
        self.SetEng(10)
        self.SetHp(self.GetHp() + self.GetEng())

    def  cutAttack(self, character):
        chance = randint(1, 100)
        if chance <= 10:
            print('Fault') #10% fault chance

        elif chance >= 95: #chance = 5%
            self.new_damage = self.GetDamage() + self.GetPwr() + ((self.GetDamage() + self.GetPwr()) * .5)
            character.ReduceHp(self.new_damage)
            print(f'{self.GetUserName()} making cutter attack! -{self.new_damage}')
        else:
            self.new_damage = self.GetDamage() + self.GetPwr()
            print(f'{self.GetUserName()} making cutter attack! -{self.new_damage}')

    def inactive(self):
        recovery = self.GetHp() + 1
        self.SetHp(recovery)
        print(f'{self.GetUserName()} recovery hp +1 current health={recovery} ')


