student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for name in student_scores:
    print(name)
    print(student_scores[name])
    convert = student_scores[name]
    if convert > 90:
        grade = "Outstanding"
    elif convert < 90 and > 80:
        grade = "Exceeds Expectations"
    elif convert < 80 and > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"

