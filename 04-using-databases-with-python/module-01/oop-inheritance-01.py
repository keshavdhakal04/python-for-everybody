class Animal: # defines the parent (base) class
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

class Dog(Animal): # dog is a child class that inherits from Animal
    def sound(self):
        print(self.name, "barks")

d = Dog("Buddy") # creates a Dog object with name "Buddy"
d.info() # calls inherited method from Animal class
d.sound() # calls method defined in Dog class