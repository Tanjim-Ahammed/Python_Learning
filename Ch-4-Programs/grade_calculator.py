marks = input("Please enter your marks: ")
marks = int(marks)

if marks >= 80:
    grade = "A+"
if marks >= 70:
    grade = "A"
if marks >= 60:
    grade = "A-"
if marks >= 50:
    grade = "B"
else:
    grade = "F"
    
print("Your grade is", grade)