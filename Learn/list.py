# collection arrays in python
"""
list
tuple
set
dictionary
"""
# LIST
fruits=["orange","10","3.14"] # we can mix the data types tooo
print(fruits[0])
 # we can perform all the operations in string
print(fruits[0:2])
print(fruits[:-1])

# to add items to list
fruits.append("apple")
print(fruits)

# to add to a particular index
fruits.insert(1,"grapes")
print(fruits)

# to remove a item from list
fruits.remove("apple")
print(fruits)

#remove item from the end
fruits.pop()
print(fruits)

#remove from a particular position
fruits.pop(0)
print(fruits)

# to clear the list compleetely
fruits.clear()
print(fruits)

# to copy the list to another copy in 2 wAYS
#fruits1=fruits.copy()
fruits1=list(fruits)
print(fruits1)

#COMBINE 2 LISTS
fruits1=["mango","banana"]
fruits2=[10,30,29]
#fruits3=fruits1+fruits2
#print(fruits3)

# extend the existing list
fruits1.extend(fruits2)
print(fruits1)