# so its a easy way of implementing collatz conjucture in python ...

n = int(input("Enter the number: "))
while n < 0 :
  n = int(input("Enter the number: "))

print('1,')
for i in range(2,n) :
  j = i
  while j > 1 :
    if j % 2 == 0 :
      j = j/2
    else:
      j = 3*j+1
    print(int(j), end=",")
  print(" All for the number "+str(i))
