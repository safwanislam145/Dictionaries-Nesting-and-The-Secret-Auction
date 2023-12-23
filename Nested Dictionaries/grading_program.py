student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for each in student_scores:
    if student_scores[each] >= 91 and student_scores[each] <= 100:
        student_grades[each] = "Outstanding"
    elif student_scores[each] >= 81 and student_scores[each] <= 90:
        student_grades[each] = "Exceeds Expectations"
    elif student_scores[each] >= 71 and student_scores[each] <= 80:
        student_grades[each] = "Acceptable"
    elif student_scores[each] <= 70:
        student_grades[each] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades) 
