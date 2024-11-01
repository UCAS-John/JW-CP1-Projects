#John Wangwang SkillPractice: Error Handling Calculator

def calculate(x: float, y: float, operator: str):
    """
    Get x and y and operation want to perform
    return False if divide by 0
    return the result of operation
    """
    if operator == '+':
        return x+y
    elif operator == '-':
        return x-y
    elif operator == '*':
        return x*y
    else:
        if y == 0:
            return False
        else:
            if operator == '/':
                return x/y
            else:
                return x%y

def main():

    while True:
        try:
            x = float(input("Enter your first number: "))
            y = float(input("Enter your second number: "))
        except ValueError:
            print("Please type in number.")
            continue

        operator = input("Type in operation you like to perform: ")

        #Check if input operation is valid
        if operator not in ['+','-','*','/','%']:
            print("Please type in number between 1-4")
            continue

        result = calculate(x, y, operator)

        if not result:
            print("You can't divide by 0 !!!!!")
            continue
        
        print(f"{x} {operator} {y} = {result}")

        choice = input("Press 1 to stop\nOr type any key to continue: ")

        if choice == '1':
            break
        else:
            continue

if __name__ == "__main__":
    main()