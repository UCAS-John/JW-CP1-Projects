
def histogram(number: list):
    for (i, num) in enumerate(number):
        print(f"{i+1}:", end = "")
        for j in range(num):
            print("*", end = "")
        print("")

def main():

    while True:
 
        num_input = input("Enter at least 6 number seperated by space: ")  
        
        number = num_input.split()  
        number = [int(num) for num in number]  

        if not all(isinstance(num, int) for num in number):
            print("Please Enter an integers!")
            continue
        if len(number) < 6:
            print("Please Enter at least 6 number!")
            continue
        else:
            break

    histogram(number)

if __name__ == "__main__":
    main()