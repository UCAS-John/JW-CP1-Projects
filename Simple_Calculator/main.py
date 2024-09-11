# John Wangwang Simple Calculator

x = float(input("Enter your first Number: "))
y = float(input("Enter your Second Number: "))

print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Exponentiation\n7.Floor division")
decision = int(input("Enter the Number of your desire operator: "))

if decision == 1:
    print(x+y)
elif decision == 2:
    print(x-y)
elif decision == 3:
    print(x*y)
elif decision == 4:
    print(x/y)
elif decision == 5:
    print(x%y)
elif decision == 6:
    print(x**y)
elif decision == 7:
    print(x//y)
else:
    print("Operator number Error")
