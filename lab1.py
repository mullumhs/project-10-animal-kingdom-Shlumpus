"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a base class for an animal and derived classes for specific 
               types of animals in an animal kingdom program.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a class named Animal that represents a generic animal in an animal kingdom.
# This class should have an initialiser with at least three attributes. E.g. name, age, and habitat.
# Add at least two methods for common animal behaviors. E.g. eat and sleep.

class Animal:
    def __init__(self, name, age, habitat, weight):
        self.name = name
        self.age = age
        self.habitat = habitat
        self.weight = weight
    
    def eat(self):
        print(f"{self.name} is currently munching.")
        
    def sleep(self):
        print(f"We're not sure why, but {self.name} is sleeping. #lazy")
        
    def explore(self):
        print(f"{self.name} is going on a vast adventure.")

    def __str__(self):
        return f"Animal: {self.name}, Age: {self.age}, Habitat: {self.habitat}"
    
class Bird(Animal):
    def __init__(self, name, age, habitat, weight, speed):
        super().__init__(name, age, habitat, weight)
        self.speed = speed
        
    def fly(self):
        print(f"{self.name} has taken off the ground, at a pace of {self.speed}. Fly bird, fly!")
        
    def perch(self):
        print(f"At last, {self.name} has perched.")
        

class Mammal(Animal):
    def __init__(self, name, age, habitat, weight):
        super().__init__(name, age, habitat, weight)
        
    def hunt(self):
        print(f"{self.name} is attempting, to hunt.")
        
    def scratch(self):
        print(f"Um.. {self.name} is scratching themselves. Kinda random.")
    
class Bear(Mammal):
    def __init__(self, name, age, habitat, weight):
        super().__init__(name, age, habitat, weight)
        
    def growl(self):
        print(f"")


# Create at least two derived classes from the Animal class. E.g. Bird and Fish.
# Give each of the derived classes at least one specific behavior. E.g. fly and swim.





# Create at least two instances of the Animal derived classes with different data.





# Write code that prints out the details of each animal and calls their specific behaviors.




