from Knight import  Knight
from Elf import Elf
from Wizard import Wizard


class Dragon(Knight, Elf, Wizard):
    def __init__(self, username):
        super().__init__(username)
        self.SetPwr(10)
        self.SetEng(25)
        self.SetHp(5)
        self.SetHp(self.GetHp() + self.GetEng())

