# name of class start with caps

class Student:
    # name="khadeeja"
    # age=30
    def __init__(self,name,age):  # construtor
        self.name=name
        self.age=age  #the age becomes the age of this object
        #self.displayStudent() it can also be used
        
    def displayStudent(self):
        print("name:",self.name)
        print("age:",self.age)
        

ob = Student("khadeeja",22) #create object
#ob.setStudent("khadeeja",22)
#print(ob.name)
ob.displayStudent()
ob1 = Student("Faris",19) #create  another object
#ob1.setStudent("faris",22)
# print(ob1.name)
ob1.displayStudent()
   


