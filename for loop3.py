a=[]
print("enter 5 numbers")
for i in range(4):
    num=int(input("enter num"+str(i+1)))
    a.append(num)
print(a)

sum=0
for i in a:
    sum=sum+i
print(sum)


num=int(input("enter the n terms:"))
print("the",num,"numbers are:")
sum=0
for i in range(1,num+1):
  print(i,end=" ")
  sum=sum+i
print("\nsum:",sum)