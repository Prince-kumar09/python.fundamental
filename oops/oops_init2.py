class Animal:

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def show_breed(self):
        print(self.breed)


dog1 = Dog("Tommy", "German Shepherd")

dog1.show_name()
dog1.show_breed()