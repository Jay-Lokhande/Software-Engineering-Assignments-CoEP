from prettytable import PrettyTable

table = PrettyTable()

print("Get your Result")
studentName = input("Enter Student Name: ")
rollNo = input("Enter Roll No.: ")
subCount = int(input("How many subjects are there? "))
arr = []
totalMarks = int(input("Enter total Marks: "))
i = 1
table.field_names = ["Subject", f'Marks out of {totalMarks}']
Marks = 0
while i <= subCount:
    subjectName = input("Subject Name: ")
    marks = float(input(f'Enter Marks of Subject {subjectName}: '))
    if marks > totalMarks:
        print("marks can't" f'be greater than total marks ({totalMarks}) please enter marks of subject {subjectName} again')
        continue
    Marks += marks
    table.add_row([subjectName, marks])
    arr.append(marks)
    i += 1

average_marks = Marks/(subCount*totalMarks)
percentage = average_marks*100
table.preserve_internal_border
print("******************************************************************************")
print("Student Name: ", studentName)
print("Roll No.: ", rollNo)

print(table)
print("Percentage: ", round(percentage, 2),"%")
if percentage >= 80:
    print("i-division")
elif percentage >= 70:
    print("ii-division")
elif percentage >= 50:
    print("iii-division")
elif percentage >= 45:
    print("iv-division")
elif percentage >= 35:
    print("iv-division")
else:
    print("Fail")
