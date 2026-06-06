a=int(input("enter number:"))
if(a%5==0 & a%3==0):
    print("divisible by 5 and 3")
else:
    print("not divisible by 5 and 3")


a=int(input("enter number:"))
if(a%2==0):
    print("even")
else:
    print("odd")

mark=int(input("enter your mark:"))
if(mark<35):
    print("poor student")
elif(mark>35 and mark<70):
    print("avg student")
elif(mark>70 and mark<100):
    print("good student")

