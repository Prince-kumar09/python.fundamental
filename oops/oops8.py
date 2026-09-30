class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Invalid balance")


account1 = BankAccount("Prince", 5000)

account1.set_balance(7000)
print(account1.get_balance())

account1.set_balance(-500)
print(account1.get_balance())