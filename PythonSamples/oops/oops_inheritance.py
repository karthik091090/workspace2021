
class AnimalParent:
    def pp(self):
        print("I am inside animal parent class")
        
class Animal:
    name='bingo'
    def a(self):
        print("I am inside animal class")
    
class Mammal(Animal,AnimalParent):
    def b(self):
        print("I am inside Mammal class")
        
        
mam=Mammal()
mam.b()
mam.a()
print(mam.name)
mam.pp()