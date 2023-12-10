#PROBLEM 5

#so we have a word and a sentence , lets finf out how many times we can find the word in the sentence
"""
there is an issue here , for example my sentence is: The butterfly can fly. and my word is fly.
so how many times should i count the word fly? there is a fly in the butterfly. 
accorfing to the question, im counting it!

"""

sentence = input("Enter: the sentence: ")
word = input("Enter the word: ")

cnt = 0
for index in range(len(sentence)) :
  if sentence[index] == word[0] : 
    if sentence[index: index+ len(word)] == word :
      cnt += 1

print(cnt)       

