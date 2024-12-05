def format(number: int):
    if number/100 >= 1:
        print(f"{number}|", end="")
    elif number/10 >= 1:
        print(f"{number} |", end="")
    else: 
        print(f" {number} |", end="")

def line():
    for i in range(52):
        print("-", end="")

def main():

    num_list = list(range(1,13))s

    line()
    print("\n   |", end="")
    for number in num_list:
        format(number)
    print("")
    line()

    for number in num_list:
        print("")
        format(number)
        for multi in num_list:
            format(number*multi)
        print("")
        line()

if __name__ == "__main__":
    main()