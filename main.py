student_name = input("Enter your name :")
marks1 = float(input("Enter your marks for Mathematics (Out of hundred) :"))
marks2 = float(input("Enter your marks for English (out of hundred) :"))
marks3 = float(input("Enter your marks for Urdu (Out of hundred) :"))
Total_marks = 300
Total_obtained = marks1 + marks2 + marks3
Average = (marks1 + marks2 + marks3)/3
Average = round(Average)
print(f"This is the report card of {student_name}")
print(f"Your average marks were {Average}")
print(f"You got {Average} percent marks")




if Average >= 90:
    print("You passed the exam with an A+ grade")
elif Average >= 80:
    print("You passed the exam with an A grade")
elif Average >= 70:
    print("You got a B on your exam")
elif Average >= 60:
    print("You got a C on your exam")
    print("You should study harder next time")
elif Average <= 50:
    print("You failed the exam")
    print("You should work harder next time")