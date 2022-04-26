class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def myfunc(self):
        print("Hello my name is " + self.name)

obj1=person('karthik',32)
print(obj1.name)
print(obj1.age)

obj1.myfunc()