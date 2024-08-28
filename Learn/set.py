# it has no order and it has no index

fruits={"apple","orange","banana"}
print(fruits) #{'banana', 'apple', 'orange'}

# we can only access the items no by index but through loop

for x in fruits:
    print(x)

# to add items
fruits.add("grapes")

# to remove items
fruits.remove("orange")
print(fruits)

#when we use pop here it is not sure that the item removes is the last one beacuase it has no index
fruits.pop()
print(fruits)
