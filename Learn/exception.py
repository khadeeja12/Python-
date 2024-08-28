
# try:
#     age=int(input("enter your age:"))
#     print(age)
# except:
#     print("please enter a valid number")


try:
    #print(x) it is a Nameerror
    #print(10/0) #it is a ZeroDivisionError
    age=int(input("enter your age:"))
except NameError:
    print("variable not defined")
except ZeroDivisionError:
    print("divison with zero not possible")
except:
    print("error")


