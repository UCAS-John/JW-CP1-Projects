# John Wangwang Simple Calculator

text = "Your answer is"
x = None
y = None
decision = None
x = float(input("Enter your first Number: "))
y = float(input("Enter your Second Number: "))

print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Exponentiation\n7.Floor division")
decision = int(input("Enter the Number of your desire operator: "))

if decision == 1:
    print(text, x+y)
elif decision == 2:
    print(text, x-y)
elif decision == 3:
    print(text, x*y)
elif decision == 4:
    print(text, x/y)
elif decision == 5:
    print(text, x%y)
elif decision == 6:
    print(text, x**y)
elif decision == 7:
    print(text, x//y)
else:
    print("Operator number Error")
