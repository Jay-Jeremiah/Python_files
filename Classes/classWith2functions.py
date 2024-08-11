class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    
    def myDetails(self):
        print("Hi my name is",self.name)

intro = Person("Harry", 23)

intro.myDetails()