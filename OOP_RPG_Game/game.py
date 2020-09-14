from Knight import Knight
from Elf import Elf
from Wizard import Wizard
from Beginner import Beginner
from Dragon import Dragon
from random import randint


wins = 0
lose = 0
gamer1_class = "0"
nickname = input("Please enter a gamer name: ")
rank = 0


while 1:
    char = Beginner(nickname)
    print(f'Welcome to the Magic Game! (WINS:{wins} / LOSE:{lose}')
    print("Choose a mode: ")
    choice = int(input("1.Single play\n2.Multiplay\nChoice: "))

    if choice == 1:
        print("You have chosen SINGLE PLAY MODE")
        char = Beginner(nickname)
        bot = Dragon("Dragon")
        print(f'Your name is: {char.GetUserName()}')
        print(f'Dragon name is: {bot.GetUserName()}')
        rank_type = str(char.__class__.__name__)

        while (char.GetHp() > 0 and bot.GetHp() > 0):
            turn_a = randint(0, 2)
            turn_b = randint(0, 4)
            if (char.GetHp() > 0 and bot.GetHp() > 0):
                if (wins > 1):
                    rank = (input("Choose a rank\n[1]Knight\n[2]Wizard\n[3]Elf\n"))
                if rank =="1":
                    char = Knight(nickname)
                elif rank == "2":
                    char = Wizard(nickname)
                elif rank == "3":
                    char = Elf(nickname)
                elif rank == "4":
                    char = Beginner(nickname)
                else:
                    char = Beginner(nickname)


                while (char.GetHp() > 0 and bot.GetHp() > 0):
                    turn_a = randint(0, 4)
                    turn_b = randint(0, 4)
                    if (char.GetHp() > 0 and bot.GetHp() > 0):
                        while (turn_a > 0):
                            if (turn_a != 0):
                                try:
                                    if (turn_a == 1):
                                        char.cutAttack(bot)
                                        print(f'{bot.GetUserName()} have only {bot.GetHp()} remaining\n')
                                    elif (turn_a == 2):
                                        char.wizardAttack(bot)
                                        print(f'{bot.GetUserName()} have only {bot.GetHp()} remaining\n')
                                    elif (turn_a == 3):
                                        char.extendedAttack(bot)
                                        print(f'{bot.GetUserName()} have only {bot.GetHp()} remaining\n')
                                        char.cure()
                                except:
                                    char.commonAttack(bot)
                                    print(f'{bot.GetUserName()} have only {bot.GetHp()} remaining\n')
                            turn_a = turn_a - 1

                if (turn_b > 0):
                    if (turn_b != 0):
                        try:
                            if (turn_b == 1):
                                bot.cutAttack(char)
                                print(f'{char.GetUserName()} have only {char.GetHp()} remaining\n')
                            elif (turn_b == 2):
                                bot.wizardAttack(char)
                                print(f'{char.GetUserName()} have only {char.GetHp()} remaining\n')
                            elif (turn_b == 3):
                                bot.extendedAttack(char)
                                print(f'{char.GetUserName()} have only {char.GetHp()} remaining\n')
                            elif (turn_b == 4):
                                bot.cure()
                        except:
                            bot.commonAttack(char)
                            print(f'{char.GetUserName()} have only {char.GetHp()} remaining\n')
                    turn_b = turn_b - 1


        if (char.GetHp() <= 0):
            print(f'{bot.GetUserName()} won!\n')
            lose = lose + 1
        else:
            print(f'{bot.GetUserName()} won!\n')
            wins = wins + 1

    elif choice == 2:
        print("You chose MULTIPLAY MODE")
        gamer1_nick = input("Please enter gamer 1 nickname: ")
        gamer2_nick = input("Please enter gamer 2 nickname: ")
        gamer1_class = input(f'Please enter {gamer1_nick} class:\n[1].Beginner\n[2].Knight\n[3].Elf\n[4].Wizard\nChoice: ')
        gamer2_class = input(f'Please enter {gamer2_nick} class:\n[1].Beginner\n[2].Knight\n[3].Elf\n[4].Wizard\nChoice: ')
        if gamer1_class == "1":
            Gamer_1 = Beginner(gamer1_nick)
        elif gamer1_class == "2":
            Gamer_1 = Knight(gamer1_nick)
        elif gamer1_class == "3":
            Gamer_1 = Elf(gamer1_nick)
        elif gamer1_class == "4":
            Gamer_1 = Wizard(gamer1_nick)
        else:
            print("Wrong choice")
            break
        if gamer2_class == "1":
            Gamer_2 = Beginner(gamer2_nick)
        elif gamer2_class == "2":
            Gamer_2 = Knight(gamer2_nick)
        elif gamer2_class == "3":
            Gamer_2 = Elf(gamer2_nick)
        elif gamer2_class == "4":
            Gamer_2 = Wizard(gamer2_nick)
        else:
            print("Wrong choice!")
            break


        while (Gamer_1.GetHp() > 0 and Gamer_2.GetHp() > 0):
            turn_a = randint(0, 4)
            turn_b = randint(0, 4)

            if (Gamer_1.GetHp() > 0 and Gamer_2.GetHp() > 0):
                while (turn_a > 0):
                    if (turn_a != 0):
                        try:
                            if (turn_a == 1):
                                Gamer_1.cutAttack(Gamer_2)
                                print(f'{Gamer_2.GetUserName()} have only {Gamer_2.GetHp()} remaining\n')
                            elif (turn_a == 2):
                                Gamer_1.wizardAttack(Gamer_2)
                                print(f'{Gamer_2.GetUserName()} have only {Gamer_2.GetHp()} remaining\n')
                            elif (turn_a == 3):
                                Gamer_1.extendedAttack(Gamer_2)
                                print(f'{Gamer_2.GetUserName()} have only {Gamer_2.GetHp()} remaining\n')
                            elif (turn_a == 4):
                                Gamer_1.cure()
                        except:
                            Gamer_1.commonAttack(Gamer_2)
                            print(f'{Gamer_2.GetUserName()} have only {Gamer_2.GetHp()} remaining\n')
                    turn_a = turn_a - 1

                while (turn_b > 0):
                    if (turn_b != 0):
                        try:
                            if (turn_b == 1):
                                Gamer_2.cutAttack(Gamer_1)
                                print(f'{Gamer_1.GetUserName()} have only {Gamer_1.GetHp()} remaining\n')
                            elif (turn_b == 2):
                                Gamer_2.wizardAttack(Gamer_1)
                                print(f'{Gamer_1.GetUserName()} have only {Gamer_1.GetHp()} remaining\n')
                            elif (turn_b == 3):
                                Gamer_2.extendedAttack(Gamer_1)
                                print(f'{Gamer_1.GetUserName()} have only {Gamer_1.GetHp()} remaining\n')
                            elif (turn_b == 4):
                                Gamer_2.cure()
                        except:
                            Gamer_2.commonAttack(Gamer_1)
                            print(f'{Gamer_1.GetUserName()} have only {Gamer_1.GetHp()} remaining\n')
                    turn_b = turn_b - 1

            if (Gamer_1.GetHp() <= 0):
                print(f'{Gamer_2.GetUserName()} won!')
                break
            if (Gamer_2.GetHp() <= 0):
                print(f'{Gamer_1.GetUserName()} won!')
                break










