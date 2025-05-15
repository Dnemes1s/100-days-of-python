def format_change(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"
    
def function_1(text):   # This function gets an input and adds them together in a string and then returns the output to the "output" var
    return text + text

def function_2(text):
    return text.title() # This function gets the output from function 1 and uses it as the input

output = function_2(function_1("Hello"))    # How function 2 can get the output of function 1 and use it as an input
print(output)   # Returns the output from function 2 


formatted_string = format_change("stevie", "wonder")

print(formatted_string)

