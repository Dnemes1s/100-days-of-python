# # Ceaser cypher coder and de coder
def encode(word, shift):
    for letter in word: # Checks each letter

        if letter == " ":
            encored_word.append(letter) # Places a space if there is one
        
        if letter != " ":
            index = alphabet.index(letter) + shift  # Finds the individual letters index in the list of characters and adds the shift number
            index %= len(alphabet) # Makes sure the shifted value is within 26
            add_letter = alphabet[index]    # Finds the alphabet character based off the new index number
            encored_word.append(add_letter) # Adds the letter to a list for output later
            

def decode(word, shift):
    for letter in word:

        if letter == " ":
            encored_word.append(letter)
        
        if letter != " ":
            index = alphabet.index(letter) - shift
            index %= len(alphabet)
            add_letter = alphabet[index]
            encored_word.append(add_letter)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to the ceaser cypher coder/decoder")

# word = input("Input a word or phrase: ")
# shift = int(input("Input the shift: "))
encored_word = []
cont = True
while cont: # When true the program will keep looping and asking if you want to encode or decode
    encode_or_decode = input("Do you want to encode or decode ? (Type 'encode' or 'decode') ").lower()

    if encode_or_decode == "encode":
        word = input("Input a word or phrase: ").lower()    # Makes the input all lower
        shift = int(input("Input the shift: ")) # Asks for the amount you want to shift
        encode(word, shift) # Runs encode function

    if encode_or_decode == "decode":
        word = input("Input a word or phrase: ").lower()
        shift = int(input("Input the shift: "))
        decode(word, shift) # Runs decode functions

    output = "".join(encode_or_decode) # Outputs the encoded word and joins it so its not seperated
    print(output)   # Prints outpiut
    encored_word = []   # Clears the encoded word var for a new one if the user wishes to restart
    restart = input("Would you like to restart ? y/n\n")    # asks the user if they want to encode/decode again
    if restart == "n":  # If used chooses no the program will end
        cont == False   # Sets state to false and escapes the while loop to end
        print("Goodbye")
    
