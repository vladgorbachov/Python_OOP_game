from KindDescription import KindDescription
from random import randint



class Beginner(KindDescription):
    def commonAttack(self, character):
        chance = randint(1, 100)
        if chance <= 15:
            if self.__class__.__name__ == "Elf" and character.__class__.__name__ == "Knight":
                character.ReduceHp(self.GetDamage() * 3 + ((self.GetDamage() * 3) * .10))
                print(
                    f'{self.GetUserName()} doing a regular common attack -{(self.GetDamage() * 3 + ((self.GetDamage() * 3) * .10))}')

            elif self.__class__.__name__ == "Wizard" and character.__class__.__name__ == "Elf":
                character.ReduceHp(self.GetDamage() * 3 + ((self.GetDamage() * 3) * .10))
                print(
                    f'{self.GetUserName()} doing a regular common attack -{(self.GetDamage() * 3 + ((self.GetDamage() * 3) * .10))}')

            elif self.__class__.__name__ == "Knight" and character.__class__.__name__ == "Wizard":
                character.ReduceHp(self.GetDamage() * 3 + ((self.GetDamage() * 3) * .10))
                print(
                    f'{self.GetUserName()} doing a regular common attack -{(self.GetDamage() * 3 + ((self.GetDamage() * 3) * .10))}')


            elif self.__class__.__name__ == "Beginner":
                character.ReduceHp(self.GetDamage() * 3)
                print(f'{self.GetUserName()} doing a regular common attack -{(self.GetDamage() * 3)}')

            else:
                character.ReduceHp(self.GetDamage() * 3)
                print(f'{self.GetUserName()} doing a regular common attack - {(self.GetDamage() * 3)}')

        else:
            if self.__class__.__name__ == "Elf" and character.__class__.__name__ == "Knight":
                character.ReduceHp(self.GetDamage() + ((self.GetDamage()) * .10))
                print(
                    f'{self.GetUserName()} doing a regular common attack -{(self.GetDamage() + self.GetDamage() * .10)}')

            elif self.__class__.__name__ == "Wizard" and character.__class__.__name__ == "Elf":
                character.ReduceHp(self.GetDamage() + ((self.GetDamage()) * .10))
                print(
                    f'{self.GetUserName()} doing a regular common attack -{(self.GetDamage() + self.GetDamage() * .10)}')

            elif self.__class__.__name__ == "Knight" and character.__class__.__name__ == "Wizard":
                character.ReduceHp(self.GetDamage() + ((self.GetDamage()) *  .10))
                print(f'{self.GetUserName()} doing a regular common attack -{(self.GetDamage() + self.GetDamage() * .10)}')

            elif self.__class__.__name__ == "Beginner":
                character.ReduceHp(self.GetDamage())
                print(f'{self.GetUserName()} making common attack! -{self.GetDamage()}')

            else:
                character.ReduceHp(self.GetDamage())
                print(f'{self.GetUserName()} making common attack! -{self.GetDamage()}')



