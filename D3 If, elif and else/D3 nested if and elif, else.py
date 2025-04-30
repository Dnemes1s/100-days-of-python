print("Welcome to the pizzaa ordering program!")
size = input("What size pizza do you want? (S, M, L): ")
peperoni = input("Do you want peperoni? (Y, N): ")
extra_cheese = input("Do you want extra cheese? (Y, N): ")
#Gathering initial inputs from user

#Setting the bill to 0 at the start
bill = 0

# Getting the size of the pizza and the apropriate price
if size == "S" or size == "s": # Added or to check for both upper and lower case
    bill += 15
    print("Small pizza is $15")    #Small pizza
elif size == "M" or size == "m":
    bill += 20
    print("Medium pizza is $20")   #Medium pizza
elif size == "L" or size == "l":
    bill += 25
    print("Large pizza is $25")    #Large pizza
else:
    print("Invalid size selected.")


#Geting the price of the peperoni
if peperoni == "Y" or peperoni == "y":
    if size == "S" or size == "s":  # Added or to check for both upper and lower case
        bill += 2
        print("Small peperoni is $2")   #Small pizzas have less peperoni so adding price discrepancy
    else:
        bill += 3
        print("Medium/Large peperoni is $3")

#Getting the price of the extra cheese
if extra_cheese == "Y" or extra_cheese == "y":
    bill += 1
    print("Extra cheese is $1")

#Printing the final bill
print(f"Your final bill is: ${bill}")