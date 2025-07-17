# class operator:
#     def __init__(self,pages):
#         self.pages=pages
        
#     def __add__(self,other):
#         totalpages=self.pages_+


class A:
    def add(self):
        print("I am method inside A")
        
class B:
    def add(self):
        print("I am method inside B")
        

obj=B()
obj.add()