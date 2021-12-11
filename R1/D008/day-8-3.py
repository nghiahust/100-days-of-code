def encrypt(text, shift):
    encrypted_txt = ""
    for char in text:
        encrypted_txt += alphabet[(alphabet.index(char) + shift) % len_abc]
    print(f"Your ecrypted text is: {encrypted_txt}")

def decrypt(text, shift):
    decrypted_txt = ""
    for char in text:
        decrypted_txt += alphabet[alphabet.index(char) - shift]
    print(f"Your decrypted text is: {decrypted_txt}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
len_abc = len(alphabet)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("not found")

