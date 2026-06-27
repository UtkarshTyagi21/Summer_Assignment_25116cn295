#WAP to create marksheet generation system.
name = input("Enter Student Name: ") #Input student details
roll_no = input("Enter Roll Number: ")

math = int(input("Enter Math marks: ")) #Input marks for 3 subjects
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

total = math + science + english
percentage = (total/3)

if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 50:
    grade = "B"
elif percentage >= 35:
    grade = "C"
else:
    grade = "Fail"

#Display Marksheet
print("\n" + "=" * 30)
print(f"      STUDENT MARKSHEET      ")
print("=" * 30)
print(f"Name: {name}")
print(f"Roll No: {roll_no}")
print("-" * 30)
print(f"Math: {math}/100")
print(f"Science: {science}/100")
print(f"English: {english}/100")
print("-" * 30)
print(f"Total: {total}/300")
print(f"Percent: {percentage:.2f}%")
print(f"Grade: {grade}")
print("=" * 30)
