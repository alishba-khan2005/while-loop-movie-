
username=str(input("enter your username: "))
if username=="alishba khan":
    print("username not available")
elif username=="alish khan":
    print("username not available")
else:
    print(username)
    email=str(input("enter your email address: "))

#selecting movie
command = input("do you want to continue downloading movies yes/no")
while command.lower() in ["yes" , "yess"]:
    print("select category")
    print("1:Action\n 2:Sci Fi\n 3.Rom-Com\n 4.mysterious")
    category=int(input("enter your value 1 till 4:"))
    if category == 1:
        print("The A team")
        print("Divergent")
        print("Maze Runner")
    elif category == 2:
        print("Avengers")
        print("The Martian")
        print("Gravity")
    elif category == 3:
        print("School")
        print("Tall Girl")
        print("Nancy")
    elif category == 4:
       print("The mystery Island")
       print("The space")
       print("Anatomy")
    else:
       print("inavlid category")
    command = input("do you want to continue downloading movies (yes/no):")
    if command.lower() not in {"yes","yess","y","YES"}:
      break
    print("thankyou for downloading ")