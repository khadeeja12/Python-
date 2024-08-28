# sometimes we want to divide the project into seperate files ...so we can import it and use it

#we can execure the calc.py operations in this file

# #import calc
# print( calc.add(10,20))
# print(calc.sub(10,30))

 
 #if we can only want specific operation 
from Learn.calculations.calc import add
print(add(10,20))
