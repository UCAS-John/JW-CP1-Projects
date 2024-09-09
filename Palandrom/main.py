# John Wangwang Palandrom

word = None
word = input("Enter word: ")
word = word.upper()

if word[::-1] == word:
    print("This word is a palindrome.") 
else:
    print("This word isn't a palindrome.") 