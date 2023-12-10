#PROBLEM 6

# so its a easy way of implementing collatz conjucture in python ...

n = int(input("Enter the number: "))
while n < 0 :
  n = int(input("Enter the number: "))

print('1, Number:1')
for i in range(2,n) :
  j = i
  while j > 1 :
    if j % 2 == 0 :
      j = j/2
    else:
      j = 3*j+1
    print(int(j), end=",")  
    # Dear TA , im not sure if i can use end , but i think its the only way to make the output look clean!
  print(" Number:"+str(i))
