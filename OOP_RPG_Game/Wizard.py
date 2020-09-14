from Beginner import Beginner
from random import randint


class Wizard(Beginner):

    def __init__(self, username):
        super().__init__(username)
        self.SetInt(10)
        self.SetEng(5)
        self.SetHp(self.GetHp() + self.GetEng())


    def cure(self):
        self.AddHp(self.GetInt())
        print(f'{self.GetUserName()} did a cure! + {self.GetInt()}')


    def wizardAttack(self, character):
        chance = randint(1, 100)
        if chance <= 10:
            print(f'Fault')
        elif chance >= 95:
            self.new_damage = (self.GetDamage() + self.GetInt() + ((self.GetDamage() + self.GetInt()) * .5))
            character.ReduceHp(self.new_damage)
            print(f'{self.GetUserName()} making wizard attack! -{self.new_damage}')
        else:
            self.new_damage = self.GetDamage() + self.GetInt()
            character.ReduceHp(self.new_damage)
            print(f'{self.GetUserName()} making wizard attack! -{self.new_damage}')

    def inactive(self, character):
        character.ReduceHp(1)
        print(f'Life leak done -1 to {character.GetUserName()} {character.GetHp}')


