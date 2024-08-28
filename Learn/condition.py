# if statement
age=18
#age=int(input("enter your age:"))
if age>=18:
    print("eligible for voting")
else:
    print("not eligible for voting")
# print(type(age))

#if elseif
age=int(input("enter your age:"))
if age>=18:
    print("eligible for voting")
    print("another title")
elif age>=12:
    print("another one")
else:
    print("not eligible for voting")


