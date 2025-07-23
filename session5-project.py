# 📝 Grades Classifier - Session 5: elif Statement and Logical Operators
# Welcome to Python School! Let's help you process your exam scores like a pro 📚✨
# We will update our last session's project to assign grades based on boundaries instead
# of a simple pass/fail output. We will also use

# Print welcome message

print("Welcome to Python School Grade Calculator!")

# Ask for student name

name = input("Enter your name: ")

# Take marks for three subjects (out of 100 each)

english = float(input("Enter English marks (out of 100): "))
computer = float(input("Enter Computer marks (out of 100): "))
maths = float(input("Enter Maths marks (out of 100): "))

# ➕ Addition to Last Project: Print a warning if either of the subjects' marks
# exceed 100. This should only be a warning and program should continue with invalid inputs.
# Hint: Use a single if with an appropriate logical operator to combine conditions.

if maths > 100 or computer > 100 or english > 100:
  print("\n⚠️ Warning: One or more marks exceed 100! Calculation will continue anyway.\n")

# Total marks possible

total_possible = 300

# Total obtained

total_obtained = maths + computer + english

# Calculate average and percentage

average = total_obtained / 3
percentage = (total_obtained / total_possible) * 100

# Round for nicer output

average = round(average, 2)
percentage = round(percentage, 2)

# Print student report

print("\nStudent Report for", name)
print("----------------------------------------")
print(f"Maths: {maths}/100")
print(f"computer: {computer}/100")
print(f"English: {english}/100")
print(f"Total: {total_obtained}/300")
print(f"Average: {average}")
print(f"Percentage: {percentage}%")

# Display results

print("\n Final Grade:")
if percentage >= 90:
    print("A+")
elif percentage >= 80:
    print("A")
elif percentage >= 70:
    print("B")
elif percentage >= 60:
    print("C")
elif percentage >= 50:
    print("D")
else:
    print("F")

# ℹ️ Update this part of pass/fail decision from last session project to
# instead assign a grade based on following boundaries.




# Encouraging message

print("\nKeep working hard and keep learning! 💡📘\n")

# 💡 Notes for learners:
# - Arithmetic: + for addition, / for division, () controls order (precedence).
# - Comparison: >= checks "greater than or equal to".
# - A comparison returns True or False, which we can print as a result.