import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word_list=["camel","strawberry","shark","baboon","deer","whale","glass"]

random_word=random.choice(word_list)
length=len(random_word)
print((length)*"_")
correct_letters=[]
live=6
gameover=False
print(HANGMANPICS.pop(0))
while not gameover:

    letter_guess = input("Guess a letter: ")
    display = ""

    for letter in random_word:

        if letter == letter_guess:
            display += letter
            correct_letters.append(letter_guess)
        elif letter in correct_letters:
            display+=letter
        else:

            display += "_"

    print(display)
    if letter_guess not in random_word:
        live -= 1
        print(f"You have {live} live")
        print(HANGMANPICS.pop(0))


        if live==0:
            gameover=True
            print(f"You lose the word was {random_word}")



    if "_" not in display:
        gameover=True
        print("You won!")

