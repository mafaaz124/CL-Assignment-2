class BankAccount:
    def __init__(self, pin):
        self.__pin = float(pin)
        self.balance = 0
        self.dCounter = 0
        self.wCounter = 0
        self.history = []

    def verify_pin(self, user_pin):
        return self.__pin == float(user_pin)

    def deposit(self, amount):
        if amount < .01:
            print("Insufficient funds.\n")
            return
        else:   
            self.balance += amount
            self.dCounter += 1
            self.history.append(self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.\n")
        else:
            self.balance -= amount
            self.wCounter += 1
            self.history.append(self.balance)


    def get_balance(self):
        return self.balance
    
    def statement(self):
        print(f"Your current balance is ${self.balance:.2f}") 
        print("Transaction History: ")
        for num in self.history:
            print(f"${num:.2f}")
        print(f"You made {self.dCounter} deposits") 
        print(f"You made {self.wCounter} withdraws") 


def main():
    while True:    
        try:
            pin = float(input("Please set an account PIN: "))
            account = BankAccount(pin)
            break
        except ValueError:
            print("Please enter a valid PIN number.\n")
        

    while True:
        try:    
            entered_pin = float(input("Please enter your account PIN to login: "))
            if account.verify_pin(entered_pin):
                print("Login successful.\n")
                break
            else:
                print("Incorrect PIN. Please try again.\n")
        except UnboundLocalError:
            print("Please enter a valid PIN number.\n")
        except ValueError:
            print("Please enter a valid PIN number.\n")

    while True:
        action = input("Enter your action (Deposit, Withdraw, Balance, Statement, Exit): ").lower()

        if action == "deposit":
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
                if amount < .01:
                    print("Insufficient funds.\n")
                else:
                    print(f"${amount:.2f} has been deposited.\n")

            except ValueError:
                print("Please enter a valid number to deposit.\n")

        elif action == "withdraw":
            try:    
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
                if amount > account.get_balance():
                    pass
                else:
                    print(f"${amount:.2f} has been withdrawn.\n")

            except ValueError:
                print("Please enter a valid number to withdraw.\n")
        elif action == "balance":
            print(f"Current balance: ${account.get_balance():.2f}\n")

        elif action == "statement":
            account.statement()

        elif action == "exit":
            print("Logging out.\n")
            try:    
                entered_pin = float(input("Please enter your account PIN to login: "))
                if account.verify_pin(entered_pin):
                    print("Login successful.\n")
                    break
                else:
                    print("Incorrect PIN. Please try again.\n")
            except ValueError:
                print("Please enter a valid PIN number.\n")
                break

        else:
            print("Invalid action.\n")
            

main()
