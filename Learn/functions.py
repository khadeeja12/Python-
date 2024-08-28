def wish():
    print("welcome")

wish()

# using arguements
def call(name,age):
    print("welcome",name,"you are",age)

call("khadeeja",22) # this order is also important

call(name="khadeeja",age=22) #now it is correctly goes without order



#sum using return statement
def sum(a,b):  # or we can use sum(a=10,b=20) here if the value is not passed by the function
    c=a+b
    return c

#print(sum(10,20))
s=sum(10,20)
print(s)

# we can take n number of arguements
def sum(*arg):  # here this arg is come as tuple because we dont chnage the value of it
    sum=0
    #print(arg)     #(1, 2, 3)
    for x in arg:
        sum+=x
    return sum

print(sum(1,2,3)) #6


# if we pass name along with the value in function
def sum(**arg):  
    print(arg['n1'])
    return sum

print(sum(n1=1,n2=2,n3=3)) 



