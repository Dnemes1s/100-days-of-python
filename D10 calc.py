def add(num1, num2):
    sum = num1 + num2


def subtract(num1, num2):
    sum = num1 - num2


def multiply(num1, num2):
    sum = num1 * num2
    

def divide(num1, num2):
    sum = num1 / num2
    held_num = sum

function = input("What do you want to do ? Add(+) Subtract(-) Multiply(*) or Divide(/)")
num1 = input("Input first number: ")
num2 = input("Input second number: ")
calculate = True


while calculate:
    held_num = 0
    if function == "+":
        add(num1, num2)

    elif function == "-":
        subtract(num1, num2)

    elif function == "*":
        multiply(num1, num2)

    elif function == "/":
        divide(num1, num2)

    



