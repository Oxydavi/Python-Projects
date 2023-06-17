import random
import sys

player = int()


def zxc():
    try:
        global player
        player = int(input("Enter your choose,  from 1 to 6: "))
    except ValueError:
        print("Error, choose from 1 to 6")
        zxc()


zxc()

if player == 1 or player <= 6:
    print("Your choise:", player, "of 6")
else:
    print("you are degan")
    zxc()

bullet = random.randint(1, 6)

if bullet == player:
    print("You loose")
    sys.exit(0)
else:
    print("Congratulations, you survived")
    sys.exit(0)



