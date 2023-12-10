#so we have a word and a sentence , lets finf out how many times we can find the word in the sentence

sentence = input("Enter: the sentence: ")
word = input("Enter the word: ")

cnt = 0
for index in range(len(sentence)) :
  if sentence[index] == word[0] : 
    if sentence[index: index+ len(word)] == word :
      cnt += 1

print(cnt)       

