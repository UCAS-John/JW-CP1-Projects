#John Wangwang ProficiencyTest: Secret Cypher

def encode(string: str, shift: int) -> str:
    string = string.upper()
    strings = list(string)
    for i in range(len(string)):
        Ascii = ord(string[i]) + shift
        if Ascii > ord('Z'):
            Ascii
        strings[i] = chr(Ascii)
    cipher = "".join(strings)
    return cipher

def decode(string: str, shift: int) -> str:
    string = string.upper()
    strings = list(string)
    for i in range(len(string)):
        Ascii = ord(string[i]) - shift
        strings[i] = chr(Ascii)
    cipher = "".join(strings)
    return cipher

choice = int(input("""1. Encode Cipher
2. Decode Cipher
Enter your choice: """))

code = input("Type your strings: ")
shiftValue = int(input("Enter amount of shift: "))

print(f"Before: {code}")
if choice == 1:
    print(f"After {encode(code, shiftValue)}")
elif choice == 2:
    print(f"After {decode(code, shiftValue)}")
else:
    print("Error please enter the corresponding number!")