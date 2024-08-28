fruits=["apple","orange","mango"]  # same as for tuple and set
for x in fruits:
    print(x)

str="welcome to python programming"  # here we consider it as a list and iterating
for x in str:
    print(x)

# this can be used in another simple way
for x in "apple":
    print(x)

# continue here orange is not printed others are printed
for i in fruits:
    if i=="orange":
        continue
    print(i)

# break only apple is printed
for i in fruits:
    if i=="orange":
        break
    print(i)

# we use range 
for i in range(10): # here it creates a range of 0 to 9
    print(i)

for i in range(1,11): # here it creates a range of 1 to 10
    print(i)

sum=0
for i in range(1,11):
    sum+=i
print(sum)


# int object is not iterable . therefore we use collections or range() for iteration in for



