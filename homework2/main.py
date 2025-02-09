students =(
    ("Alice",85,90,88),
    ("Bob" ,78,81,74),
    ("Charlie",92,89,95),
    ("Diana",70,75,80)
)



student_name=input("Enter the student's name")


found = False
for student in students:
    if student[0].lower()== student_name.lower():
        found = True
        total_marks = sum(student[1:])
        print(f"The total marks for {student[0]}are {total_marks}.")
        break
  

if not found:
    print("Student not found in the register")
