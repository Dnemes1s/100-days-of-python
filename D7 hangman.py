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

game_over = False
correct_letters = []
incorrect_letters = []

while not game_over:
    guess = input("guess a letter: \n").lower()
    # Makes all inputs lower case

    display = "" 

    
    for letter in word:
        
        if letter == guess:
            display += letter
            correct_letters.append(letter)

        elif letter in correct_letters:
            display += letter    
        else:
            display += "_"
            
            
    if guess not in correct_letters:
        lives -= 1
        incorrect_letters.append(guess)
        

    print(f"Incorrect letters: {", ".join(incorrect_letters)}")
    print(display)
    print(f"You have {lives} lives remaining\n")

    if "_" not in display:

        game_over = True
        print("You win")