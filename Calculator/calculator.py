import math
import sys
while True:
    # исключения и переменные
    END = "Enter number, dumbass"  # типо введите числа
    NEZ = "No enter 0"  # нельзя вводить 0
    OP = "Input your operation," \
         "if you want to know the list of operators write 'ops' " # введите оператор
    try:
        num1: float = float(input("Enter first number: "))
        num2: float = float(input("Enter second number: "))
        tt = num1 / num2
    except ValueError:
        print(END)
        sys.exit(0)
    except ZeroDivisionError:
        print(NEZ)
        sys.exit(0)
    if ValueError:
        if ZeroDivisionError:
            op: str = input(OP)
        else:
            sys.exit(0)
        # Операции + - и тд.
        if op == "ops":
            print("+, -, *, /, sqrt (√x), ^ (number1^number2), !")
        elif op == "+":
            zxc = f"{num1} + {num2} = {num1 + num2}"
        elif op == "-":
            zxc = f"{num1} - {num2} = {num1 - num2} "
        elif op == "*":
            zxc = f"{num1} * {num2} = {num1 * num2} "
        elif op == "/":
            zxc = f"{num1} / {num2} = {num1 / num2} "
        elif op == "sqrt":
            zxc = f"√2 from {num1} is", math.sqrt(num1),",", \
                  f"also √2 from {num2} is", math.sqrt(num2)
        elif op == "^":
            zxc = f"{num1} ^ {num2} is {num1**num2}"
        elif op == "!":
            num1_1 = int(num1)
            num2_1 = int(num2)
            f_num1 = math.factorial(num1_1)
            f_num2 = math.factorial(num2_1)
            print(f"!{num1} is {f_num1}, !{num2} is {f_num2}")
        else:
            print("Entered wrong operator")
            sys.exit(0)
        print(zxc)