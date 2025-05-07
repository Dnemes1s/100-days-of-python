# # Ceaser cypher coder and de coder
def encode(word, shift):
    for letter in word:
        
        if letter == " ":
            idk.append(letter)
        
        if letter != " ":
            index = alphabet.index(letter) + shift
            index %= len(alphabet)
            add_letter = alphabet[index]
            idk.append(add_letter)
            

def decode(word, shift):
    for letter in word:
        
        if letter == " ":
            idk.append(letter)
        
        if letter != " ":
            index = alphabet.index(letter) - shift
            index %= len(alphabet)
            add_letter = alphabet[index]
            idk.append(add_letter)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to the ceaser cypher coder/decoder")

# word = input("Input a word or phrase: ")
# shift = int(input("Input the shift: "))
idk = []
cont = True

while cont:
    encode_or_decode = input("Do you want to encode or decode ? (Type 'encode' or 'decode') ").lower()

    if encode_or_decode == "encode":
        word = input("Input a word or phrase: ")
        shift = int(input("Input the shift: "))
        encode(word, shift)

    if encode_or_decode == "decode":
        word = input("Input a word or phrase: ")
        shift = int(input("Input the shift: "))
        decode(word, shift)

    poo = "".join(idk)
    print(poo)
    idk = []
    restart = input("Would you like to restart ? y/n\n")
    if restart == "n":
        cont == False
        print("Goodbye")
    
