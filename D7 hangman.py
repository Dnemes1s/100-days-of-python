import random

words = ["python", "java", "javascript", "html", "css"]
# list of words
lives = 7
# number of lives
word = random.choice(words)
# choosing a random word from the list
hangman_counter =-1
# Counter to go through hangman pics

# ascii art for hangman
hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 ||   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 |||  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 |||  |
 |    |
      |
=========''', '''
  +---+
  |   |
  O   |
 |||  |
 | |  |
      |
=========''',
""]


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

game_over = False   # Game state
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
        incorrect_letters.append(guess) # Adds wrong guessed letters into a var
        hangman_counter += 1    # Iterates the hangman ascii depending on remaining lives

    if lives == 0:
        game_over = True    # Changes the game state to escape the loop if the users lives are 0
        print("You lose")
        

    print(f"Incorrect letters: {", ".join(incorrect_letters)}") # Prints out the letters user has guessed thats wrong
    print(hangmanpics[hangman_counter]) # Displays hangman state
    print(display) # Displays word
    print(f"You have {lives} lives remaining\n") # Displays lives

    if "_" not in display:

        game_over = True
        print("You win")
        # Game win state. Tests to see if there are any _ in the display var. If none it ends the game and player wins

print("Try again")

