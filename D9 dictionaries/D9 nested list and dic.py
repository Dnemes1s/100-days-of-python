capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested lists in dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijion"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# How to print from a nested list in a dic

# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])    # Getting item from a nested list in a list

travel_log = {      # Dict that has a dictionary nested and then a list inside that dictionary
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijion"],
    },
    "Germany": {
        "num_times_visited": 5,
        "cities_visited":["Stuttgart", "Berlin"],
    }
}

print(travel_log["Germany"]["cities_visited"][0]) # Printing from the list nested in the dictionary thats nested in a dictionary

