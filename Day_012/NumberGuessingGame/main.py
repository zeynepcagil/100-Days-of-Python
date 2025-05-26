import random

start_ques =input("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100. \n Choose a difficulty. Type 'easy' or 'hard': ")
numb=random.randrange(0,100)
isTrue=False



def check():
    if numb == guess:
        global isTrue
        isTrue = True
        print(f"You got it! The answer was {numb}.")
    elif numb> guess:
        print("Too low. \n Guess again.")
    elif numb<guess:
        print("Too high. \n Guess again.")
    else:
        isTrue = False
def game():
    global guess_count
    global isTrue
    global guess
    while not guess_count==0 and isTrue==False:
        guess = int(input(f"You have {guess_count} attempts remaining to guess the number. \n Make a guess: "))
        guess_count -= 1

        check()
    if guess_count==0:
        print(f"You've run out of guesses. The number was {numb} ")
if start_ques=='easy':
    guess_count=10
    game()
if start_ques=='hard':
    guess_count=5
    game()
