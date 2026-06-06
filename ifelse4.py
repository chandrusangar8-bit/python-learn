a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
operation=input("add/sub/mul/div:")
if(operation=="add"):
    print(a+b)
elif(operation=="sub"):
    print(a-b)
elif(operation=="mul"):
    print(a*b)
elif(operation=="div"):
    print(a/b)
else:
    print("invalid operation")


sp=int(input("enter your sp:"))
if(sp>=70):
    print("you are eligible")
    name=input("enter your name:")
    dpt=input("enter your dpt:")
    location=input("enter your location")
    print("name:",name)
    print("dpt:",dpt)
    print("location:",location)
else:
    print("you are not eligible")