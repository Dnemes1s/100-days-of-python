student_scores = [78, 85, 56, 95, 88, 76, 23, 89, 84, 134, 87, 93, 94, 64, 97, 43, 142, 82, 81, 80, 79, 77, 22, 74, 34, 163, 74, 70]
# Gets scores from a list of students
max_score = 0
# Sets a variable to hold the maximum score

# Loop through each score in the list and compare it with the current maximum score
# If the current score is greater than the maximum score,update the maximum score

for score in student_scores:
    if score > max_score:
        max_score = score

# Print the maximum score
print(f"The maximum score is {max_score}.")