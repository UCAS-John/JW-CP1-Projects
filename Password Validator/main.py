#John Wangwang SkillPractice: Password Validator

def requirement(password: str) -> dict:
    """
    Get parameter password as string
    return dictionary of the requirements needed for strong password
    """
    special_char = ['@','#','$','%','&']

    required = {
        "length": False,
        "number": False,
        "special": False,
    }

    if len(password) >= 8:
        required["length"] = True
    
    for char in password:
        if char.isnumeric():
            required["number"] = True
            break
    
    for char in password:
        if char in special_char:
            required["special"] = True
            break

    return required

def valid(required: dict) -> bool:
    """
    Get parameter requirement dictionary 
    return True if all requirement is True
    return False if not
    """

    if all(required.values()):
        return True
    else:
        return False

def main():              

    while True:

        password = input("Enter your password: ") #Get user password

        required = requirement(password)

        #Check if Password is strong
        if valid(required):
            print("Your password is strong!")
            break
        else:
            print("Your password is didn't meet the criteria below:")

        #Print out requirement needed for the password to be strong
        if not required["length"]:
            print("Your password must be at least 8 characters long.")
        if not required["number"]: 
            print("Your password should include at least 1 number.")
        if not required["special"]:
            print("Your password should have at least 1 special character (Examples: @, #, $, %, *, &) ")

if __name__ == "__main__":
    main()