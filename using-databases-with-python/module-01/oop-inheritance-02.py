# Parent Class: Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

# Child Class: Dog
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # Call parent constructor 
        self.breed = breed

    def details(self):
        print(self.name, "is a", self.breed)

d = Dog("Buddy", "Golden Retriever")
d.info()      # Parent method
d.details()   # Child method

""""
super() function is used to call the parent class’s methods. 
In particular, it is commonly used in the child class’s __init__() method to initialize inherited attributes. 
This way, the child class can leverage the functionality of the parent class.
"""