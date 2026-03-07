class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3) #creates an object of the 'Dog' Class, with name as 'Buddy' and age as 3

print(dog1.name) #prints 'Buddy'
print(dog1.species) #prints 'Canine'

#dog1.name: Accesses the instance attribute name of the dog1 object.
#dog1.species: Accesses the class attribute species of the dog1 object.