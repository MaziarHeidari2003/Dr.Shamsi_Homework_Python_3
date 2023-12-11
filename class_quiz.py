# calcaulate the sum of the prime numbers in the input string
numbers = input("Enter the numbers seperated bt comma: ")
sum = 0
for i in numbers:
  if i != "," :
    j = int(i)
    m = 1 
    cnt = 0
    while m <= j :
      if j % m == 0 :
        cnt += 1
      m += 1
    if cnt == 2 :
      sum += j

print(sum)      
          

