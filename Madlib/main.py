# John Wangwang Madlib

default_value = "..."
word = [default_value] * 5

for i in range(0, 5):
    word[i] = input(f"Type your {i+1} word! : ")

MadLib = f"In the Morning, you wake up and found {word[0]}.\nYou are very {word[2]} to found out that you just got {word[1]}!\nLater that day, you began {word[3]} for your {word[4]}.\nYou become depressed and {word[2]}, you find out that you forget to pay your tax.\nYou are now a fraud, but you still continue to {word[3]}."

print(MadLib)