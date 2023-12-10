sentence = input("Enter: the sentence: ")
word = input("Enter the word: ")

cnt = 0
for index in range(len(sentence)) :
  if sentence[index] == word[0] : 
    if sentence[index: index+ len(word)+1] == word :
      cnt += 1

print(cnt)       