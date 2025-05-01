#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# Adding variables for the letters, numbers and symbols

print("Welcome to the PyPassword Generator!")
# Welcoming the user
# Asking the user for the number of letters, symbols and numbers
letters_count = int(input("How many letters would you like in your password?\n"))
symbols_count = int(input("How many symbols would you like?\n"))
numbers_count = int(input("How many numbers would you like?\n"))
# Getting the user input for the number of letters, symbols and numbers

password_list = []
# Creating an empty list for the password

for char in range(1, letters_count + 1):
    password_list.append(random.choice(letters))
    print(password_list)
# Adding the letters to the password list
#The (random.choice(letters)) function will choose a random letter from the letters list and add it to the paassword list

for char in range(1, symbols_count + 1):
    password_list.append(random.choice(symbols))
    print(password_list)
# Adding the symbols to the password list
#The (random.choice(symbols)) function will choose a random symbol from the symbols list and add it to the paassword list

for char in range(1, numbers_count + 1):
    password_list.append(random.choice(numbers))
    print(password_list)
# Adding the numbers to the password list
#The (random.choice(numbers)) function will choose a random number from the numbers list and add it to the paassword list

random.shuffle(password_list)
print(password_list)
# Shuffling the password list

password = ""
# Creating an empty string for the password

for char in password_list:
    password += char
    print(password)
# Adding the characters to the password string

print(f"Your password is: {password}")
# Printing the password
# This will print the password