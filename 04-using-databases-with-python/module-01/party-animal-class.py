class PartyAnimal:
    def __init__(self): # constructor method (runs automatically when object is created)
        self.x = 0
        print("I am a Constructor")
    
    def Party(self):
        self.x = self.x + 1
        print("So far,", self.x)
    
    def __del__(self): # destructor method (runs when the object is about to be destroyed)
        print("I am a Destructor", "and self.x is", self.x)


an = PartyAnimal() # creates an object of class PartyAnimal
an.Party() # prints: So far, 1
an.Party() # prints: So far, 2

an = 42 # removes reference to the PartyAnimal object, so Python destroys it
print(an) # prints 42