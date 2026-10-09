class Animal:

    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):

    def speak(self):
        print("Dog barks")


class Cat(Animal):

    def speak(self):
        print("Cat meows")
dog1 = Dog()
cat1 = Cat()
dog1.speak()
cat1.speak()

