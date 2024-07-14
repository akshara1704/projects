choice = 0
l1 = []
l2 = []
l3 = []
grade=" "
while choice != 1:
    name = input("Enter your name = ")
    eng = int(input("Enter marks for eng ="))
    hindi = int(input("Enter marks for hindi ="))
    maths = int(input("Enter marks for maths ="))
    chem = int(input("Enter marks for chem ="))
    physics = int(input("Enter marks for physics ="))
    percentage = (eng + hindi + maths + chem + physics) / 5
    print(name, "achieve percentage = ", percentage)
    # grading system if percentage lies in range
    if percentage <= 100 and percentage >= 70:
        grade = "A"
        print(name, "achieve grade", grade)
    elif percentage <= 69 and percentage >= 55:
        grade = "B"
        print(name, "achieve grade", grade)
    elif percentage <= 54 and percentage >= 42:
        grade = "C"
        print(name, "achieve grade", grade)
    elif percentage <= 41 and percentage >= 33:
        grade = "D"
        print(name, "achieve grade", grade)
    elif percentage <= 32:
        grade = "!Fail!"
        print(name, "achieve grade", grade)
    l1.append(name)
    print(l1)
    l2.append(percentage)
    print(l2)
    l3.append(grade)
    print(l3)
    choice = int(input("Enter 1 to end the process and press 0 to continue"))
for i in range(0,len(l1)):
    f=open("Names_of_student","a")
    f.write("name= ")
    f.write(l1[i])
    f.write(" ")
    f.write("percentage= ")
    f.write(str(l2[i]))
    f.write(" ")
    f.write("grade= ")
    f.write(l3[i])
    f.write(" ")
    f.write("\n")
    f.close()


