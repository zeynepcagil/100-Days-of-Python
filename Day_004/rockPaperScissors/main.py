import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
game=[rock,paper,scissors]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
console_choice=random.randint(0,2)

if user_choice==console_choice:
    print(f"You choose: \n {game[user_choice]} \n Computer choose: \n {game[console_choice]} ")
    print("It's a draw")
elif user_choice==2 and console_choice==1:
    print(f"You choose: \n {game[user_choice]} \n Computer choose: \n {game[console_choice]} ")
    print("You win!")
elif user_choice==2 and console_choice==0:
    print(f"You choose: \n {game[user_choice]} \n Computer choose: \n {game[console_choice]} ")
    print("You lose!")
elif user_choice==1 and console_choice==2:
    print(f"You choose: \n {game[user_choice]} \n Computer choose: \n {game[console_choice]} ")
    print("You lose!")
elif user_choice==1 and console_choice==0:
    print(f"You choose: \n {game[user_choice]} \n Computer choose: \n {game[console_choice]} ")
    print("You win!")
elif user_choice==0 and console_choice==2:
    print(f"You choose: \n {game[user_choice]} \n Computer choose: \n {game[console_choice]} ")
    print("You win!")
elif user_choice==0 and console_choice==1:
    print(f"You choose: \n {game[user_choice]} \n Computer choose: \n {game[console_choice]} ")
    print("You lose!")