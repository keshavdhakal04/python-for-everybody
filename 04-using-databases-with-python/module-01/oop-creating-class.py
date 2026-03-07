class Dog: #create a class named "Dog"
    species = "Canine"  # Class attribute (shared by all instances of the class)

    def __init__(self, name, age): # Constructor/Initializer (runs automatically when object is created, and initialize object data)
        self.name = name 
        self.age = age 

# self refers to the current object, allowing each object to store and access its own data.
# self.name and self.age are instance attributes, unique to each Dog object created from the class.
