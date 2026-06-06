name=input("enter your name:")
maths_mark=input("enter maths mark:")
physics_mark=input("enter physics mark")
chemistry_mark=input("enter chemistry mark:")
m=int(maths_mark)
p=int(physics_mark)
c=int(chemistry_mark)
total=m+p+c
avg=(m+p+c)/3
pc=(total/300)*100
print("total mark:",total)
print("avg:",avg)
print("pc:",pc)
if(m>=p and m>=c):
  print("highest mark:",m)
elif(p>=m and p>=c):
  print("highest mark:",p)
else:
  print("highest mark:",c)

if(avg>=90):
  81
  print("A grade")
elif(avg>=70 and avg<90):
  print("B grade")
elif(avg>=50 and avg<70):
  print("C grade")
else:
  print("fail")