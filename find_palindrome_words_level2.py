#PROBLEM 3

word = input("Enter the word: ")
new_word = ''
for char in word :
  new_word = char + new_word
if new_word == word :
  print("The word is palindrome")
else:
  print("The word is not palindrome")  