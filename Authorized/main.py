#John Wangwang ProficiencyTest: Authorized

def authorize(user: str, authorized: list) -> bool:
    """
    Get in username and list of authorized user
    return True if user is authorized
    """
    if user in authorized:
        return True
    return False

def check_admin(user: str, admin: list) -> bool:
    """
    Get in username and list of admins
    return True if user is admin
    """
    if user in admin:
        return True
    return False

def main():

    authorized = ['John', 'Sam', 'Kaneki', 'Masachika', 'Godzilla', 'Alisa', 'Trin', 'Top']
    admins = ['John', 'Top']

    user = input("Type in your username: ") #Get username

    #check for authorized user and admin
    if not authorize(user, authorized):
        print("You are not authorized!")
    elif check_admin(user, admins):
        print("Welcome Adminstrator!")
    else:
        print("Welcome Authorized User!")

if __name__ == "__main__":
    main()