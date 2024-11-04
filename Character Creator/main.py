#John Wangwang RAID: Character Creator

character = {
    "Name" : "",
    "Class" : "",
    "Race" : "",
    "Health" : 0,
    "Strength" : 0,
    "Dexterity" : 0,
    "Intelligence" : 0
}

classes = ['Barbarian', 'Cleric', 'Knight', 'Mage', 'Ranger', 'Rogue']
races = ['Human', 'Elf', 'Orc', 'Dwarf', 'Fairy', 'Giant']

def main():

    print("You're going to create a character please fill in the following information")

    character["Name"] = input("Character name: ")

    for (i,role) in zip(range(1,7), classes):
        print(f"{i}.{role}")

    while True:
        try:
            num = int(input("Type in your choice of class(1-6): "))
        except ValueError:
            print("Please type in number between 1-6!")
            continue
        if num not in range(1,7):
            print("Please type in number between 1-6!")
            continue
        break

    character["Class"] = classes[num-1]

    for (i,race) in zip(range(1,7),races):
        print(f"{i}.{race}")

    while True:
        try:
            num = int(input("Type in your choice of class(1-6): "))
        except ValueError:
            print("Please type in number between 1-6!")
            continue
        if num not in range(1,7):
            print("Please type in number between 1-6!")
            continue
        break

    character["Race"] = races[num-1]

    while True:
        try:
            character["Health"] = int(input("Character Health: "))
            character["Strength"] = int(input("Character Strength: "))
            character["Dexterity"] = int(input("Character Dexterity: "))
            character["Intelligence"] = int(input("Character Intelligence: "))
        except ValueError:
            print("Please type in number!")
            continue
        break

    print("\nThis is your chracter information:")
    for info in character:
        print(f"{info}: {character[info]}")   

if __name__ == "__main__":
    main()