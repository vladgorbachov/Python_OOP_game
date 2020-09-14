class KindDescription():

    def __init__(self, username):
        self.__username = username
        self.__hp = 100
        self.__magic_mana = 100
        self.__damage = 5
        self.__pwr = 0  # power
        self.__eng = 0  # energy
        self.__int = 0  # intellect
        self.__mob = 0  # mobility

    def GetUserName(self):
        return self.__username

    def SetUserName(self, new_username):
        return self.__username

    def GetHp(self):
        return self.__hp

    def SetHp(self, new_hp):
        return self.__hp

    def GetDamage(self):
        return self.__damage

    def SetDamage(self, new_damage):
        return self.__damage

    def GetPwr(self):
        return self.__pwr

    def SetPwr(self, new_pwr):
        return self.__pwr

    def GetEng(self):
        return self.__eng

    def SetEng(self, new_eng):
        return self.__eng

    def GetInt(self):
        return self.__int

    def SetInt(self, new_int):
        return self.__int

    def GetMob(self):
        return self.__mob

    def SetMob(self, new_mob):
        return self.__mob

    def ReduceHp(self, damage_amount):
        self.__hp = self.__hp - damage_amount

    def AddHp(self, health_amount):
        self.__hp = self.__hp + health_amount




