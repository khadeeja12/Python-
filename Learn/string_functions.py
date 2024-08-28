# remove the whitespaces
str1="   apple    "
print(str1.strip())

# to lowercase anduppercase
print(str1.lower())
print(str1.upper())

# replace a character with another character
print(str1.replace("a","x")) #  xpple

# split the string into list(array is called as list in python)
s="apple,orange,mango"
print(s.split(",")) # ['apple', 'orange', 'mango']

#find a string
x="orange" in s
print(x) # true

# print the name along with a text using format function
name="khadeeja"
txt="my name is {} and my age is {}"
age=30
print(txt.format(name,age)) # my name is khadeeja and my age is 30


