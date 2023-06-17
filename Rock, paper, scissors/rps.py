import sys
import random


def qwe():
    print("Do you wanna play again? Type 'yes 'or 'no': ")
    play = input("")
    if play == "yes":
        zxc()
    elif play == "no":
        print("Thanks for the game")
        sys.exit(0)
    else:
        qwe()


def zxc():
    player = input("Enter: rock, paper or scissors ")

    if player == "rock":
        player_c = True
    elif player == "paper":
        player_c = True
    elif player == "scissors":
        player_c = True
    else:
        print("You dumb ass")
        sys.exit(0)

    while player_c:
        computer = random.randint(1, 3)

        if computer == 1:
            computer = "rock"
        elif computer == 2:
            computer = "paper"
        else:
            computer = "scissors"
        print("computer has: ", computer)

        if player == "rock" and computer == "paper" or \
            player == "paper" and computer == "scissors" or \
            player == "scissors" and computer == "rock":
            print("You loose")
            qwe()
        elif computer == "rock" and player == "paper" or \
            computer == "paper" and player == "scissors" or \
            computer == "scissors" and player == "rock":
            print("You win")
            qwe()
        else:
            print("Draw")
            qwe()


zxc()
