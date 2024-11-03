import art #Import art.py
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):  # THE FUNCTION FOR CAESAR CIPHER

    output_text = ""

    if encode_or_decode == "decode": #THIS WILL TURN THE SHIFT AMOUNT INTO NEGATIVE ALLOWING US TO SHIFT THE LETTER BACKWARDS HENCE DECODING
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet: #THIS WILL ALLOW THE ITEMS IN THE WORD TO NOT BE INCLUDED IN THE DECODING BUT STILL BE ADDED TO THE FINAL OUTPUT TEXT
            output_text += letter
        else: #THIS IS THE PROCESS OF ENCODING OR DECODING WHICH SHIFTS THE LETTER FROM THE INITIAL INDEX TO THE SHIFT AMOUNT GIVEN BY THE USER
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")


while True: #THIS LOOP GIVES CONTROL TO THE USER WHETHER THEY WOULD WANT TO KEEP GOING ON ENCODING OR DECODING
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    ask = input("Enter 'yes' if you want continue or 'no' if you don't want to continue:").lower()
    if ask == 'yes':
        continue
    elif ask == 'no':
        break

