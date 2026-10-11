class Animal:
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")
class Cow(Animal):
    def speak(self):
        print("Cow moos")
animal=[Dog(),Cat(),Cow()]
for animal in animal:
    animal.speak()


    #Humne kya seekha
 #Dog, Cat, Cow — teeno Animal se inherit kar rahe hain.
# Teeno classes mein same method speak() hai.
#Har class apna alag behavior perform karti hai.
# Ek hi for loop se teeno objects ka method call ho raha hai.