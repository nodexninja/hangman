from random import choice
import art
from docs import words

word = choice(words)
msg = 'You won! 🎉'
strikes = 6

output = []
for i in word:
  output.append('_')
print(art.stages[strikes])
string = ' '
print(string.join(output))
while not output.count('_') == 0:
  guess = input('Guess a letter!\n').lower()
  if (guess and not output.count(guess) > 0):
    guess = guess[0]
    if (word.count(guess) > 0):
      for i, item in enumerate(word):
        string = ' '
        if (guess == item):
          output[i] = item
      print(art.stages[strikes])
      print(string.join(output))
    else:
      strikes -= 1
      print(f'Wrong, you have {strikes} tries left!')
      print(art.stages[strikes])
      if (strikes == 0):
        msg = f'You lost! 😭\nThe word was {word}'
        break
  else:
    print('Type something valid. You can not enter the same letter again')

print(msg)
  