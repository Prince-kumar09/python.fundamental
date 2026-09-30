class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
        else:
            print("Invalid amount")
account1 = BankAccount("Prince", 5000)
account1.deposit(2000)
print(account1.get_balance())