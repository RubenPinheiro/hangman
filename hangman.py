import random
import hangman_words
import hangman_art


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6

print(hangman_art.logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while "_" in display and lives > 0:
  if lives > 0:
     print(f"{' '.join(display)}")
    
  guess = input("Guess a letter: ").lower()

  for i in range(0, len(chosen_word)):
    if chosen_word[i] == guess:
      display[i] = guess
  
  if not guess in display:
   lives -= 1
  
  if lives < 6:
   print(f'{hangman_art.stages[lives]}')

else:
  if lives == 0:
    print('You lose :(')
    print(f'Pssst, the solution was {chosen_word}.')
  else:
    print("You win!")