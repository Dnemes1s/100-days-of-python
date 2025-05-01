# Rock Paper Scissors ASCII Art
import random

# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

#user input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))

# computer choice
computer_choice = random.randint(0, 2)

if user_choice == 0 and computer_choice == 2:
    print("you choose rock")
    print(rock)
    print("computer choose scissors")
    print(scissors)
    print("You win!")

elif user_choice == 1 and computer_choice == 0:
    print("you choose paper")
    print(paper)
    print("computer choose rock")
    print(rock)
    print("You win!")

elif user_choice == 2 and computer_choice == 1:
    print("you choose scissors")
    print(scissors)
    print("computer choose paper")
    print(paper)
    print("You win!")

elif user_choice == 0 and computer_choice == 1:
    print("you choose rock")
    print(rock)
    print("computer choose paper")
    print(paper)
    print("You lose!")

elif user_choice == 1 and computer_choice == 2:
    print("you choose paper")
    print(paper)
    print("computer choose scissors")
    print(scissors)
    print("You lose!")

elif user_choice == 2 and computer_choice == 0:
    print("you choose scissors")
    print(scissors)
    print("computer choose rock")
    print(rock)
    print("You lose!")

elif user_choice == computer_choice:
    print("you choose scissors")
    print(scissors)
    print("computer choose scissors")
    print(scissors)
    print("It's a draw!")

else:
    print("Invalid input, please try again.")
    print("You lose!")
# This is a simple Rock Paper Scissors game where the user can play against the computer.
