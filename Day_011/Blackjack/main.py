import random

def play_blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    comp_cards = []
    win = True

    # Kart dağıt
    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    comp_cards.append(random.choice(cards))

    while True:
        sum_user = sum(user_cards)
        print(f"\nYour cards: {user_cards}, current score: {sum_user}")
        print(f"Computer's first card: {comp_cards[0]}")

        if sum_user > 21:
            print("You went over 21. You lose!")
            return

        answer = input("Type 'y' to get another card, type 'n' to pass: ")
        if answer == 'y':
            user_cards.append(random.choice(cards))
        else:
            break

    # Bilgisayar kart çeker
    while sum(comp_cards) < 17:
        comp_cards.append(random.choice(cards))

    sum_user = sum(user_cards)
    sum_comp = sum(comp_cards)

    print(f"\nYour final hand: {user_cards}, final score: {sum_user}")
    print(f"Computer's final hand: {comp_cards}, final score: {sum_comp}")

    if sum_comp > 21 or sum_user > sum_comp:
        print("You win!")
    elif sum_user < sum_comp:
        print("You lose!")
    else:
        print("Draw!")

# Ana oyun döngüsü
while True:
    answer = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")
    if answer.lower() == 'y':
        play_blackjack()
    else:
        print("See you later!")
        break
