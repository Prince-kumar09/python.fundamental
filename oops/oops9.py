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

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance = self.__balance - amount


account1 = BankAccount("Prince", 5000)

account1.deposit(2000)
print("Balance:", account1.get_balance())

account1.withdraw(3000)
print("Balance:", account1.get_balance())

account1.withdraw(5000)
print("Balance:", account1.get_balance())