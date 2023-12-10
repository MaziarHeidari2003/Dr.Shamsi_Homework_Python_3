#PROBLEM 1

for i in range(1,11) :
  for j in range(1,i+1) :
    x = j * i
    print(str(j)+' * '+str(i)+' = '+ str(x), end=" ")
  print()  
