#John Wangwang ProficiencyTest: Multiplication Table

def make_table(num: int) -> list:
    """
    Get number as parameter
    Return list of number multiple by 0 to 12
    """
    table = [num] * 13

    for i in range(13):
        table[i] = table[i]*(i)

    return table

def print_table(table: list):
    """
    Get table as parameter
    Print table
    """ 
    print("|", end=" ")
    for nums in table:
        print(f"{nums} |", end=" ")

def main():

    number = 0

    #Try getting an integer from user
    try:
        number = int(input("Enter your number for multiplication table: "))
    except ValueError:
        print("Please Enter Integers number")
        number = int(input("Enter your number for multiplication table: "))

    table = make_table(number)

    print_table(table)

if __name__ == "__main__":
    main()