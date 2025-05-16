def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "User has left out first name or last name"
        
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"
  

print(format_name(input("Whats your first name: "), input("Whats yout last name: ")))

length = len(format_name)
