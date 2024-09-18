#John Wangwang ProficiencyTest: Personal Information Converter

name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height in meters: ")
num = input("Enter your favorite number: ")

print(f"\nBefore Casting:\nYour name is {name}\nYour age is {age}\nYour height is {height}\nYour favorite number is{num}")

print(f"\nAfter Casting:\nYour name is {name}\nYour age is {int(age)}\nYour height is {float(height)}\nYour favorite number is {int(num)}")