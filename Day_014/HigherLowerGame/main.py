import random

stars_dict={"name": ["Nil Karaibrahimgil","Deniz Can Aydın","Zeynep Çağıl","Dilek Çağıl"], "job":["musician","3D Artist","Computer Engineer","Nurse"] , "where"  : ["Turkey","Kars","Çorum","Nevşehir" ],"fallowers" :[1000,2500,350,182]}
point=0
user_answer=""
right_answer=""

def game():
    a=random.sample(stars_dict["name"],2)
    index_a = stars_dict["name"].index(a[0])
    index_b = stars_dict["name"].index(a[1])
    print(a)

    print(f"Compare A: {a[0]}, is a {stars_dict["job"][index_a]}, from {stars_dict["where"][index_a]}")
    print(f"Agains B: {a[1]}, is a {stars_dict["job"][index_b]}, from {stars_dict["where"][index_b]}")

    if stars_dict["fallowers"][index_a]>stars_dict["fallowers"][index_b]:
        global right_answer
        right_answer="a"
    else:
       right_answer="b"
    global user_answer
    user_answer=input("Who has more followers? Type 'A' or 'B': ").lower()
game()
while user_answer==right_answer:
    point+=1
    print(f"You're right! Current score: {point}.")
    game()

print(f"You lose current score {point}. Game over")

