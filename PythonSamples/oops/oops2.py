class Practise:
    def __init__(self):
        print("inside constructor")
    
    def add(self):
        print("add")
        
obj=Practise()
obj.add()

class Emp:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def display(self):
        print(f"name is ")