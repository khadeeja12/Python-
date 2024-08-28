class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Child(Parent): # it inherits the parent class
    #pass
    def displayStudent(self):
        print("Name:",self.name)
        print("Age :",self.age)

ob=Child("khadeeja",22)
print(ob.name)  #khadeeja
ob.displayStudent()
"""output
Name: khadeeja
Age : 22 """



