class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks
student1 = Student("Prince", 80)

print(student1.get_marks())

student1.set_marks(90)

print(student1.get_marks())




class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder=account_holder
        self.__balance=balance

    def get_balance(self):
        return self.__balance
account1 = BankAccount("Prince", 5000)

print(account1.get_balance())