def calculator(num1, num2, func):
    if func == "+":
        total = num1 + num2 
    elif func == "-":
        total = num1 - num2
    elif func == "*":
        total = num1 * num2
    elif func == "/":
        if num2 == 0:
            print("Cant divide by 0")   # Error handling for divinding by zero 
            return None
        total = num1 / num2

    else:
        print("Invalid operation")
        return None
    
    print("Result: ", total)
    return float(total)

print("Welcome to the calculator")

state = True

while state:
    function = input("What function would you like to perform ? ( +, - , * , / )")
    num1 = float(input("Input your first number: "))
    num2 = float(input("Input your second number: "))
    total = calculator(num1, num2, function)

    if total is None:
        continue

    ask_to_recalc = input("Do you want to recalculate using the returned number ? (y/n)").lower()

    if ask_to_recalc == "n":
        exit_calc = input("Do you want to exit the calculator ?")
        if exit_calc == "y":
            state = False
        continue

    while True:
        function = input("What function would you like to perform ? ( +, - , * , / )")
        num3 = float(input("What number would you like to use: "))
        total = calculator(total, num3, function)
        print(total)

        if total is None:
            break

        again = input("Go again ? (y/n) ").lower()
        if again == "n":
            break


