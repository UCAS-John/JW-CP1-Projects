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

classes = [
    {"Class" : 'Barbarian',
    "Health" : 200,
    "Strength" : 150,
    "Dexterity" : 50,
    "Intelligence" : 10 },
    {"Class" : 'Cleric',
    "Health" : 130,
    "Strength" : 60,
    "Dexterity" : 100,
    "Intelligence" : 180 },
    {"Class" : 'Knight',
    "Health" : 160,
    "Strength" : 140,
    "Dexterity" : 100,
    "Intelligence" : 15 },
    {"Class" : 'Mage',
    "Health" : 100,
    "Strength" : 50,
    "Dexterity" : 40,
    "Intelligence" : 200 },
    {"Class" : 'Ranger',
    "Health" : 120,
    "Strength" : 150,
    "Dexterity" : 70,
    "Intelligence" : 80 },
    {"Class" : 'Rogue',
    "Health" : 140,
    "Strength" : 100,
    "Dexterity" : 180,
    "Intelligence" : 30 }]

races = [
    {"Race" : 'Human',
    "Health" : 1,
    "Strength" : 1,
    "Dexterity" : 1.5,
    "Intelligence" : 1.5 },
    {"Race" : 'Elf',
    "Health" : 1,
    "Strength" : 1,
    "Dexterity" : 1.5,
    "Intelligence" : 1.5 },
    {"Race" : 'Orc',
    "Health" : 2,
    "Strength" : 1.5,
    "Dexterity" : 1,
    "Intelligence" : 1 },
    {"Race" : 'Dwarf',
    "Health" : 1.5,
    "Strength" : 1.5,
    "Dexterity" : 1,
    "Intelligence" : 1 },
    {"Race" : 'Fairy',
    "Health" : 1,
    "Strength" : 1,
    "Dexterity" : 1,
    "Intelligence" : 2 },
    {"Race" : 'Giant',
    "Health" : 1.5,
    "Strength" : 2,
    "Dexterity" : 1,
    "Intelligence" : 1 }]

def main():

    print("You're going to create a character please fill in the following information")

    character["Name"] = input("Character name: ")

    for (i,role) in zip(range(1,7), classes):
        print(f"{i}.{role["Class"]}")

    while True:
        try:
            class_choice = int(input("Type in your choice of class(1-6): "))
        except ValueError:
            print("Please type in number between 1-6!")
            continue
        if class_choice not in range(1,7):
            print("Please type in number between 1-6!")
            continue
        break

    class_choice -= 1

    character["Class"] = classes[class_choice]["Class"]

    for (i,race) in zip(range(1,7),races):
        print(f"{i}.{race["Race"]}")

    while True:
        try:
            race_choice = int(input("Type in your choice of race(1-6): "))
        except ValueError:
            print("Please type in number between 1-6!")
            continue
        if race_choice not in range(1,7):
            print("Please type in number between 1-6!")
            continue
        break
    
    race_choice -= 1

    character["Race"] = races[race_choice]["Race"]

    character["Health"] = int(classes[class_choice]["Health"]*races[race_choice]["Health"])
    character["Strength"] = int(classes[class_choice]["Strength"]*races[race_choice]["Strength"])
    character["Dexterity"] = int(classes[class_choice]["Dexterity"]*races[race_choice]["Dexterity"])
    character["Intelligence"] = int(classes[class_choice]["Intelligence"]*races[race_choice]["Intelligence"])


    print("\nThis is your chracter information:")
    for info in character:
        print(f"{info}: {character[info]}")   

if __name__ == "__main__":
    main()