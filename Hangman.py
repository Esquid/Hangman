import random
import csv


def hang():
 gallows = [',--;-', '| ', '| ', '| ', '| ', '| ', '|_____']
 parts = iter([' 0 ', '/', '|', '\\', ' | ', ' A ', '/ ', '\\'])
 sequence = [1, 3, 1, 1, 2]
 for i, v in enumerate(sequence, start=1):
    for k in range(v):
        gallows[i] += next(parts)
        yield '\n'.join(gallows)
 raise StopIteration
  

def game():
  a = hang()
  with open('words.csv') as f:
   words = list(f)
   word_list = [word[:-1] for word in words if word == word.lower() and len(word) > 4]
   secret = random.choice(word_list)
   progress = ['_' for letter in secret] 
   print(progress)
   guess = input("Guess a letter: ")
   if guess in secret:
    for idx, letter in enumerate(secret):
     if letter == guess:
       progress[idx] = guess
       print(progress) 
       input("Guess a letter: ")
   while guess not in secret:
      print(next(a))
      print(progress)
      input('Guess a letter: ')
  

  


  
  
  
