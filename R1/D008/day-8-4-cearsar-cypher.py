# Library
import art

# Function to encode / decode
def ceasar_cypher(direction, text, shift):
    result = ""
    if direction == "decode":
        shift = 0 - shift
    for char in text:
        if char.isalpha():
            result += alphabet[(alphabet.index(char) + shift) % len_abc]
        else:
            result += char
    print(f"Your {direction} result is {result}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
len_abc = len(alphabet)

print(art.logo)

should_end = False

while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar_cypher(direction, text, shift)
    question = input("Do you want to restart? yes/no\n").lower()
    if question == "no":
        should_end = True
    elif question == "yes":
        should_end = False
    else:
        print("Unknown answer. Terminate the software")
        should_end = True