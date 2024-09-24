#John Wangwang SkillPractice: Pig Latin Converter

def pig_latin(word: str) -> str:

    vowels = ['a','e','i','o','u']
    pigLatin: str

    if word[0] in vowels:
        pigLatin = word + "way"
    elif word[1] in vowels:
        pigLatin = word[1:len(word)] + word[0] + "ay" 
    else:
        pigLatin = word[2:len(word)] + word[0:2] + "ay" 
    return pigLatin

string = input("Type your word: ")

print(pig_latin(string))