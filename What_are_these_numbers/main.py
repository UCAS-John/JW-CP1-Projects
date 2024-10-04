#John Wangwang ProficiencyTest: What are these numbers?

def main():

    # Comma Seperate
    num = int(input("Type Number for comma seperate: "))
    print("An integer with the comma seperate the thousands: {:,}".format(num))

    # 4 Decimal places
    dec = float(input("Type Number for 4 decimal places: "))
    print("A float with 4 decimal places: {:.4f}".format(dec))

    # Percentage
    num = float(input("Type Number for a percentage: "))
    print("A percentage: {:%}".format(num))

    # Dollar Amount
    dollar = float(input("Type Number for dollar amount: "))
    print("A dollar amount: ${:,.2f}".format(dollar))

if __name__ == "__main__":
    main()