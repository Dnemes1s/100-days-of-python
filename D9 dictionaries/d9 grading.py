student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {} # Creating an empty dictionary for the grades to go into

for name in student_scores:     # Loops through the student scores dictionary
    convert = student_scores[name]  # Getting the score of the student AKA the value from the key in the dictionary
    if convert > 90:    
        grade = "Outstanding"
    elif convert > 80:
        grade = "Exceeds Expectations"
    elif convert > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"

    student_grades[name] = grade # Adds key and new value to the empty dictionary

print(student_grades)   # Prints new dictionary 

