def add(num1, num2):
    sum = num1 + num2
    held_num = sum
    print(sum)
    return held_num


def subtract(num1, num2):
    sum = num1 - num2
    held_num = sum
    print(sum)
    return held_num

def multiply(num1, num2):
    sum = num1 * num2
    held_num = sum
    print(sum)
    return held_num

def divide(num1, num2):
    sum = num1 / num2
    held_num = sum
    print(sum)
    return held_num

function = input("What do you want to do ? Add(+) Subtract(-) Multiply(*) or Divide(/)")
num1 = float(input("Input first number: "))
num2 = float(input("Input second number: "))
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

    recirc = True 
    recalc_with_ricirc = input("Do you want to re calculate using the returned number ? (y/n)").lower()

    if recalc_with_ricirc == "n":
        recirc = False

    while recirc:
        function = input("What do you want to do ? Add(+) Subtract(-) Multiply(*) or Divide(/)")
        num3 = float(input("What number: "))
        held_num = held_num
        if function == "+":
            add(held_num, num3)

        elif function == "-":
            subtract(held_num, num3)

        elif function == "*":
            multiply(held_num, num3)

        elif function == "/":
            divide(held_num, num3)
        
        keep_going = input("Do you want to keep going ? (y/n)").lower()
        if keep_going == "n":
            recirc = False


    recalc = input("Do you want to do another calculation with fresh numbers ? (y/n)").lower()
    
    if recalc == "n":
        print("Thanks for using the calculator")
        calculate = False

    


