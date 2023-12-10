#PROBLEM 3

word = input("Enter the word: ")

con_check = True
i = 0
while i < (len(word)/2) :
  if word[i] != word[len(word) - i - 1] :
    con_check = False
    break
  i += 1

if con_check :
  print("This word is palindrome")
else:
  print("This word is not palindrome")       