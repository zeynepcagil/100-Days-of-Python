
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text,shift_amount):
    new_text = ""
    for letter in original_text:
        index=alphabet.index(letter)
        new_index=(index + shift_amount) % len(alphabet)

        new_text += alphabet[new_index]

    print(new_text)

def decrypt(crypted_tex,shift_amount):
    new_text=""
    for letter in crypted_tex:
        index=alphabet.index(letter)
        new_index=(index - shift_amount) % len(alphabet)

        new_text += alphabet[new_index]
    print(new_text)


def ceaser(original_text,shift_amount,direction):




encrypt("zlabk",2)
decrypt("bncdm",2)

