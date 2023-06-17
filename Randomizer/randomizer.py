import random
while True:
    human1 = int(input("Enter min number: "))
    human2 = int(input("Enter max number: "))
    number = random.randint(human1, human2)
    print(number)

