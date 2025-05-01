import random
# This program randomly selects a person from a list to pay for a meal.

# List of people
people = ["Anna", "Bob", "Charlie", "David", "Eva"]

# Will select a number between 0 and 4 in relation to the amount of people in the list
random_selector = random.randint(0, 4)

#Gets the random number generated and uses it to select a person from the list
selector = people[random_selector]


print(f"{selector} will pay for the meal.")
# Print the name of the person selected to pay

#More simple way to do it
selector = random.choice(people)
print(f"{selector} will pay for the meal.")

