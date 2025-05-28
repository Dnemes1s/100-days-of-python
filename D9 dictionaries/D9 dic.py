programming_dictionary = {  # Defining the dictionary
    "Bug": "An error in a program that prevents the program from running as expected.", # First part is the key and the second part is the value 
    "Function": "A piece of cose that can easily call over and over again.",    # Need to use a "" if using words
    123: "Numbers one two and three"    # Doesnt need "" if not a string
}

print(programming_dictionary["Bug"])    # How to call something in the dictionary. Only displays the value and not the key.

programming_dictionary["loop"] = "The action of doing something over and over." # Adding something to the dictionary 

empty_dict = {} # same way as making an empty list but uses {} instead

programming_dictionary["Bug"] = "A moth in your computer" # How to edit the value of a key in your dictionary

for key in programming_dictionary:
    print(key)    # This will only print out the keys in the dictionary
    print(programming_dictionary[key])  # Will print out for the value of the retreived key. Like used in ceaser cypher to call certain letters in the alphabet list  


# programming_dictionary = {} # How to wipe a dictionary
