#John Wangwang ProficiencyTest: Secret Cypher

def encode(string: str, shift: int) -> str:

    cipher = ""

    for char in string:
        if char.isupper():
            Ascii = chr((ord(char) + shift - 65) % 26 + 65)
            cipher += Ascii
        elif char.islower():
            Ascii = chr((ord(char) + shift - 97) % 26 + 97)
            cipher += Ascii

    return cipher

def decode(string: str, shift: int) -> str:

    cipher = ""

    for char in string:
        if char.isupper():
            Ascii = chr((ord(char) - shift - 65) % 26 + 65)
            cipher += Ascii
        elif char.islower():
            Ascii = chr((ord(char) - shift - 97) % 26 + 97)
            cipher += Ascii
            
    return cipher

choice = int(input("""1. Encode Cipher
2. Decode Cipher
Enter your choice: """))

code = input("Type your strings: ")
shiftValue = int(input("Enter amount of shift: "))

print(f"Before: {code}")
if choice == 1:
    print(f"After encoded with {shiftValue} shift: {encode(code, shiftValue)}")
elif choice == 2:
    print(f"After decoded with {shiftValue} shift: {decode(code, shiftValue)}")
else:
    print("Error please enter the corresponding number!")