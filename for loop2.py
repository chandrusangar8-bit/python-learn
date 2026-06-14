e_count=0
o_count=0
for i in range(1,11):
  if(i%2==0):
    e_count=e_count+1
  elif(i%2==1):
    o_count=o_count+1
print(e_count)
print(o_count)

count=0
for i in range(1,101):
  if(i%3==0 and i%5==0):
    count=count+1
print(count)