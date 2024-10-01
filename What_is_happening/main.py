#John Wangwang ProficiencyTest: What is happening?

#Define a class BankAccount
class BankAccount:

    #Define variables in BankAccount class
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    #Define the method deposit which add the deposit money to the current BankAccount balance
    def deposit(self, amount):
        if amount > 0: #check if deposit money is greater than 0
            self.balance += amount #Add deposit money to the current balance
            return True
        return False

    #Define the method withdraw which subtract the withdrawn money from the current BankAccount balance
    def withdraw(self, amount):
        if 0 < amount <= self.balance: #check if withdrawn money is greater than 0
            self.balance -= amount #Subtract withdrawn money from the current balance
            return True
        return False

    #Define the method get_balance return the balance of the BankAccount
    def get_balance(self):
        return self.balance

#Define the function create_account allowing user to create their BankAccount return account number and balance
def create_account():
    account_number = input("Enter account number: ") #Ask user for account number and store it
    initial_balance = float(input("Enter initial balance: ")) #Ask user for the initial balance of the account and store it in floating point number
    return BankAccount(account_number, initial_balance) #Create return account number and blance in BankAccount class

def main():
    accounts = {}

    #Display choice to user 
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ") #Ask user for their choice
        
        if choice == '1': #Check if choice is 1 the create an account for user
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")
        
        elif choice in ['2', '3', '4']: #if Choice is is 2,3,4

            account_number = input("Enter account number: ") #Ask user for account number
            if account_number in accounts: #Check if account exist
                account = accounts[account_number] #Assign account varaible to Accout class with account_number

                if choice == '2': #if Choice is is 2 Deposit the money in to the Account
                    amount = float(input("Enter deposit amount: ")) #Ask user for desposit amount

                    #Check if user desposit amount is valid 
                    if account.deposit(amount):
                        print(f"Deposited ${amount:.2f} successfully!")
                    else:
                        print("Invalid deposit amount.")

                elif choice == '3': #if Choice is is 3 withdrawn the money from the Account
                    amount = float(input("Enter withdrawal amount: ")) #Ask user for withdraw amount

                    #Check if user have enough money in Account
                    if account.withdraw(amount):
                        print(f"Withdrawn ${amount:.2f} successfully!")
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")
                #if choice 4 Print Current Account balance
                else:
                    print(f"Current balance: ${account.get_balance():.2f}")
                    
            #Error if accout not found
            else:
                print("Account not found.")
        
        elif choice == '5': #if choice is 5 exit the program
            print("Thank you for using our banking system. Goodbye!")
            break
        
        else: 
            print("Invalid choice. Please try again.") #Print error message if choice not in range 1 to 5

#Run Program
if __name__ == "__main__":
    main()