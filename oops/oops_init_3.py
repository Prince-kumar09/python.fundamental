#simgle inheritance
class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")

dog1 = Dog()

dog1.eat()
dog1.bark()



class Parent:
    def start(self):
        print("vehicle is starting")
class Car(Parent):
    def drive(self):
        print("car is driving")

car1=Car()
car1.start()
car1.drive()


#multilevel inheritance
class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
class puppy(Dog):
    def play(self):
        print("puppy is playing")
dog1=puppy()
dog1.play()
dog1.bark()
dog1.play()