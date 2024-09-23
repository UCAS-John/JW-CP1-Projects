#John Wangwang RAID: Anagram Creator

import random

name = ""
name = input("Type your name: ").lower()

length = len(name)
anagram = list(name)
RandomList = list(range(0, length))

for i in range(5):
    random.shuffle(RandomList)
    for j in range(length):
        anagram[j] = name[RandomList[j]]
    word = "".join(anagram)
    print(f"{i+1}. {word}")