#real world scenarios or problems
#bank accounts:saving accounts and current account inherit from bank account
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} UGX. New balance: {self.balance} UGX.")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds for withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} UGX. New balance: {self.balance} UGX.")
        self.balance -= amount
        print(f"Withdraw {amount} UGX. New balance: {self.balance} UGX.")
        
    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance} UGX")
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        #store interest rate
        self.interest_rate = interest_rate
#add a method to apply interest rate calculation
    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        #add interest to the balance
        self.balance += interest
        print(f"Interest of {interest} UGX added.New balance{self.balance} UGX.")
        
#Child class:Current account
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Withdrawal exceeds overdraft limit.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} UGX. New balance: {self.balance} UGX.")
            
            
saving= SavingsAccount("SA123", 100000, 5)
current = CurrentAccount("CA456", 50000, 10)
# Test method display
saving.display_balance()  # Output: Account Number: SA123, Balance: 100000 UGX
saving.add_interest() 
saving.withdraw(20000)
print("LB____")

current.withdraw(60000)  # Output: Withdrew 60000 UGX. New balance: -10000 UGX
current.display_balance()  # Output: Account Number: CA456, Balance: -10000 UGX
current.withdraw(20000)  # Output: Withdrawal exceeds overdraft limit.
current.display_balance()  # Output: Account Number: CA456, Balance: -10000 UGX
        