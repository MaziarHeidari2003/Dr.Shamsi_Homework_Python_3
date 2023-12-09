n = int(input("Enter the number, I will find the prime numbers less tahn it and print their fact: "))

for i in range(1,n) :
  m = 1
  cnt = 0
  while m <= i :
    if i % m == 0 :
      cnt += 1
    m += 1  
  if cnt == 2 :
    # so if we find a prime num in this iteration, we would be here trying to calculate the fact
    if i != 1 :
      x = i -1
    else: 
      x =1  
      # it could be tricki while i is 2
    fact = i 
    while x >= 1 :
      fact *= x 
      x -= 1
    print(fact)      
