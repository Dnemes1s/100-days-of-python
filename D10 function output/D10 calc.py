def add(num1, num2, held_num):
    if held_num != 0:
        sum = held_num + num1
    sum = num1 + num2
    held_num = sum
    return held_num


def subtract(num1, num2, held_num):
    sum = num1 - num2
    held_num = sum
    return held_num

def multiply(num1, num2, held_num):
    sum = num1 * num2
    held_num = sum
    return held_num

def divide(num1, num2):
    sum = num1 / num2
    held_num = sum
    return held_num

function = input("What do you want to do ? Add(+) Subtract(-) Multiply(*) or Divide(/)")
num1 = input("Input first number: ")
num2 = input("Input second number: ")
calculate = True


while calculate:

    held_num = 0
    if function == "+":
        add(num1, num2, held_num)

    elif function == "-":
        subtract(num1, num2,held_num)

    elif function == "*":
        multiply(num1, num2, held_num)

    elif function == "/":
        divide(num1, num2, held_num)

    num_3 = 0
    



