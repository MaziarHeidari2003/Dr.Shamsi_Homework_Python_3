#PROBLEM 1

m = int(input("Enter the starting nuber: "))
n = int(input("Enter the ending number: "))

while m>=n or m<=0 or n<=0 : 
  m = int(input("Enter the starting nuber: "))
  n = int(input("Enter the ending number: "))


for i in range(m,n+1) :
  for j in range(1,i+1) :
    x= i * j
    print(str(j) + ' * ' + str(i) + ' = ' + str(x), end=" ")
  print()    
