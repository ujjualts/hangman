import random
from art import stages,logo
from hangman_word import word_list

choice=random.choice(word_list)
print(logo)

print(f'Pss the choice is {choice}')

display=[]
for word in choice:
  display.append("_")

lives=6
end=False
while not end:
  print(" ".join(display))
  guess=input('enter a letter  :').lower()
  for i in range(len(choice)):
    if choice[i]==guess:
      display[i]=guess
  if guess not in choice:
    lives-=1
    if lives==0:
      print(" Sorry,you lost")
      end=True
  if display.count("_")==0 or lives<0:
    end=True
  print(stages[lives])
print(' '.join(display))
