alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         possition = alphabet.index(letter)
#         new_possition = possition + shift_amount
#         if new_possition > 25:
#             new_possition -= 26
#         cipher_text += alphabet[new_possition]
#     print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         possition = alphabet.index(letter)
#         new_possition = possition - shift_amount
#         plain_text += alphabet[new_possition]
#     print(f"The decode text is {plain_text}")

# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)

def caesar(input_text, shift_amount, direction):
    output_text = ""
    if direction == "decode":
        shift_amount *= -1
    for letter in input_text:
        possition = alphabet.index(letter)
        new_possition = possition + shift_amount
        # if new_possition > 25:
        #     new_possition -= 26
        output_text += alphabet[new_possition]
       
           
    
    print(f"The {direction} text is : {output_text}")

caesar(text, shift, direction)