import random

words = ["python", "java", "javascript", "html", "css"]
# list of words
lives = 6
# number of lives
word = random.choice(words)
# choosing a random word from the list

print(word)

# Using the variable above that got the length of the word, repalces it with underscores so the user cant see the chosen word
placeholder = ""
word_len = len(word)
for position in range(1,word_len):
    placeholder += "_"

print(placeholder)

# Greets the user and asks them to guess a letter
print("welcome to the hangman game")
print("guess the word")
print("you have 6 lives")
guess = input("guess a letter: ").lower()
# Makes all inputs lower case

display = "" 

for letter in word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)

