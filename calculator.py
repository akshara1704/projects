yourchoice=0
while yourchoice!=1:
    a=(int(input("enter first number:")))
    b=(int(input("enter second number:")))
    c=int(input("enter 1 for addition, 2 for substraction, 3 for multiplication, 4 for division: "))
    if c==1:
        print(a+b)
    elif c==2:
        print(a-b)
    elif c==3:
        print(a*b)
    elif c==4:
        print(int(a/b))
    else:
        print("enter between 1 and 4")
    yourchoice=int(input("Enter 1 to end the process and press 0 to continue"))

