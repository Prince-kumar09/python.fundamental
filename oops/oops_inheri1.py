class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    pass
Dog1=Dog()
Dog1.eat()



class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
Dog1=Dog()
Dog1.bark()
Dog1.eat()




class Animal:
    def __init__(self,name):
        self.name=name
        
    def show_name(self):
        print(self.name)
    
class Dog(Animal):
    pass
Dog1=Dog("tommy")
Dog1.show_name()