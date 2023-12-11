#PROBLEM 6

# so its a easy way of implementing collatz conjucture in python ...

n = int(input("Enter the number: "))
if n == 1 :
    print("1 is not really a good input,think about it!")
while  n <= 1 :
  n = int(input("Enter the number: "))
  
print('Number:1=> 1,')
for i in range(2,n) :
  print("Number:"+str(i)+"=>", end= " ")
  j = i
  while j > 1 :
    if j % 2 == 0 :
      j = j/2
    else:
      j = 3*j+1
    print(int(j), end=",")  
    # Dear TA , im not sure if i can use end , but i think its the only way to make the output look clean!
  print()
