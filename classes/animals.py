# Class hierarchy using Inheritance

class Animal:
    def __init__(self, name ,sex, habitat) -> None:
        self.name = name
        self.sex = sex
        self.habitat = habitat
        
class Mammal(Animal):
    unique_feature = "Mammary Glands"
    
class Bird(Animal):
    unique_feature = "Feathers"

class Fish(Animal):
    unique_feature = "Gills"
    
class Dog(Mammal):
    def walk(self):
        print("The dog is walking.")
        
class Cat(Mammal):
    def walk(self):
        print("The cat is walking")
        
class Salmon(Fish):
    def swim(self):
        print("The salmon is swimming.")
        
class Shark(Fish):
    def swim(self):
        print("The shark is swimming")
        
class Eagle(Bird):
    def fly(self):
        print("The eagle is flying.")
        
class Penguin(Bird):
    def fly(self):
        print("The penguin is not flying")