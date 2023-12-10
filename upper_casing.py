#PROBLEM 4

# ord and chr are nice built in functions in python , lets give them a try

word = input("Enter: ")
new_word = ''
for char in word :
  if 97 <= ord(char)<= 120 :
     new_char= chr(ord(char) -32)
     new_word += new_char 
  else:
     new_word += char   

print(new_word)     