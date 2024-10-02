#John Wangwang ProficiencyTest: Shopping list manager

def add(cart, item):
    cart.append(item)
    return
def remove(cart, item):
    cart.remove(item)
    return
def print_list(cart):
    for item in cart:
        print(item)

def main():

    items = input("Type your item lists (seperate by space): ")

    cart = items.split()

    while True:

        action = input("""What would you like to do?

    Enter 1 to add item

    Enter 2 to remove item

    Enter 3 to print the list
                                        
    Enter 4 to leave the list:\n""")

        if action == "1":

            item = input("Type your item to add: ")
            add(cart, item)

        elif action == "2":

            item = input("Type your item to remove: ")
            remove(cart, item)

        elif action == "3":
            print_list(cart)
        else:

            print("Have a nice day!")

            break

if __name__ == "__main__":
    main()