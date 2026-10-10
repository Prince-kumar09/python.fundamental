class Animal:
    def speak(self):
        print("Animal is speak")
class Child(Animal):
    def speak(self):
        print("Dog barks")
    

animal1=Animal()
child1=Child()
animal1.speak()
child1.speak()



class Animal:
    def speak(self):
        print("Animal is speak")
class Child(Animal):
    def speak(self):
        print("Dog barks")
class Other(Animal):
    def speak(self):
        print("other openion:")
    

animal1=Animal()
child1=Child()
other1=Other()
animal1.speak()
child1.speak()
other1.speak()