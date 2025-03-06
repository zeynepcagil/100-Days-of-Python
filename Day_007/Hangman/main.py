import random
from word_list import word_list
import hangmanPics

random_word=random.choice(word_list)
length=len(random_word)
print((length)*"_")
correct_letters=[]
live=6
gameOver: bool=False
print(hangmanPics.HANGMANPICS.pop(0))
print("You have 6 lives")
while not gameOver:

    letter_guess = input("Guess a letter: ")
    display = ""
    if letter_guess in correct_letters:
        print(f"You've already guessed {letter_guess}")

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
        print(f"You guessed {letter_guess} ,that's not in the word. You have {live} live")
        print(hangmanPics.HANGMANPICS.pop(0))


        if live==0:
            gameOver=True
            print(f"You lose the word was {random_word}")



    if "_" not in display:
        gameOver=True
        print("You won!")

