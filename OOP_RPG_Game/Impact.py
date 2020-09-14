from Knight import Knight
from Elf import Elf
from Wizard import Wizard
from Beginner import Beginner
from random import randint


g1nick = input("(G1) What`s your nickname?\n>")
g2nick = input("(G2) What`s your nickname?\n>")

g1class = int(input("(G1) Please choose a class: (1.Elf 2.Knight 3.Wizard\n"))
g2class = int(input("(G2) Please choose a class: (1.Elf 2.Knight 3.Wizard\n"))

g1 = Beginner(g1nick)
g2 = Beginner(g2nick)


if g1class == 1:
    g1 = Elf(g1nick)
elif g1class == 2:
    g1 = Knight(g1nick)
elif g1class == 3:
    g1 = Wizard(g1nick)

if g2class == 1:
    g2 = Elf(g2nick)
elif g2class == 2:
    g2 = Knight(g2nick)
elif g2class == 3:
    g2 = Wizard(g2nick)



mind_1 = g1.__class__.__name__
mind_2 = g2.__class__.__name__
print(f'(G1) selected {mind_1}')
print(f'(G2) selected {mind_2}')


g1_wins = 0
g2_wins = 0
g1_init_hp = g1.GetHp()
g2_init_hp = g2.GetHp()



i = 1
while i < 4:
    g1.SetHp(g1_init_hp)
    g2.SetHp(g2_init_hp)
    while g1.GetHp() > 0 and g2.GetHp() > 0:
        attack_g1 = 1
        attack_g2 = 1
        print(f'Round: {i}')
        defend_randomizer_1 = randint(0, 100)
        defend_randomizer_2 = randint(0, 100)
        g1_choice = int(input("Please enter an attack (1.Attack/2.Defend"))
        g2_choice = int(input("Please enter an attack (1.Attack/2.Defend"))


        if (g1_choice == 1):
            print(f'G1{g1.GetUserName()} turn!')
            if (attack_g2 == 1):
                if mind_1 == "Elf":
                    rsk_kill_elf = randint(0, 1)
                    if rsk_kill_elf == 0:
                        g1.inactive()
                        g1.extendedAttack(g2)
                    elif rsk_kill_elf == 1:
                        g1.inactive()
                        g1.commonAttack(g2)
                    elif mind_1 == "Knight":
                        rsk_kill_knight = randint(0, 1)
                        if rsk_kill_knight == 0:
                            g1.inactive()
                            g1.cutAttack(g2)
                        elif rsk_kill_knight == 1:
                            g1.inactive()
                            g1.commonAttack(g2)
                    elif mind_1 == "Wizard":
                        rsk_kill_wizard = randint(0, 1)
                        if rsk_kill_wizard == 0:
                            g1.inactive()
                            g1.wizardAttack(g2)
                        elif rsk_kill_wizard == 1:
                            g1.inactive()
                            g1.commonAttack(g2)
                    print(f'End of G1{g1.GetUserName()} turn!\n')
                    print(f'{g2.GetUserName()} have {g2.GetHp()} remaining hp')

                elif (attack_g2 == 0):
                    print(f'{g2.GetUserName()} defend from your attack!')

            elif (g1_choice == 2):
                if defend_randomizer_1 <= 20:
                    print(f'{g1.GetUserName()} defend success!')
                    attack_g1 = 0
                else:
                    print(f'{g1.GetUserName()} defend failed :-(')
                    attack_g1 = 1


            if (g1_choice == 1):
                print(f'G2{g2.GetUserName()} turn!')
                if attack_g1 == 1:
                    if mind_2 == "Elf":
                        rsk_kill_elf_1 = randint(0, 1)
                        if rsk_kill_elf_1 == 0:
                            g2.inactive()
                            g2.extendedAttack(g1)
                        elif rsk_kill_elf_1 == 1:
                            g2.inactive()
                            g2.commonAttack(g1)

                    elif mind_2 == "Knight":
                        rsk_kill_knight_1 = randint(0, 1)
                        if rsk_kill_knight_1 == 0:
                            g2.inactive()
                            g2.cutAttack(g1)
                        elif rsk_kill_knight_1 == 1:
                            g2.inactive()
                            g2.commonAttack(g1)

                    elif mind_2 == "Wizard":
                        rsk_kill_wizard_1 = randint(0, 1)
                        if rsk_kill_wizard_1 == 0:
                            g2.inactive()
                            g2.wizardAttack(g1)
                        elif rsk_kill_wizard_1 == 1:
                            g2.inactive()
                            g2.commonAttack(g1)

                    print(f'End of {g2.GetUserName()} turn\n')
                    print(f'{g1.GetUserName()} have {g1.GetHp()} remaining hp')

                elif attack_g1 == 0:
                    print(f'{g1.GetUserName()} defending from your attack!')

            elif (g2_choice == 2):
                if defend_randomizer_2 <= 20:
                    print("G2 Defending success!")
                    attack_g2 = 0
                else:
                    print("G2 Defending failed :-(")
                    attack_g2 = 1
            if (g1.GetHp() <= 0):
                print(f'{g2.GetUserName()} won!')
                g2_wins = g2_wins + 1
            if (g2.GetHp() <= 0):
                print(f'{g1.GetUserName()} won!')
                g1_wins = g1_wins + 1

        i = i + 1


print("\nResults: ")
print(f'{g1.GetUserName()} has won {g1_wins} times')
print(f'{g2.GetUserName()} has won {g2_wins} times')







