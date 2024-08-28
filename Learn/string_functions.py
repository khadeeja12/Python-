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
txt1="my name is {0} and my age is {1}"
txt2="my name is {1} and my age is {0}"
age=30
print(txt.format(name,age)) # my name is khadeeja and my age is 30
print(txt1.format(name,age)) # my name is khadeeja and my age is 30
print(txt2.format(name,age)) # my name is 30 and my age is khadeeja

#print the name along with quotes we use an escape slash
name1="\"khadeeja\""
print(name1) # "khadeeja"

# find the location of character
print(name.index("a")) # 2

# checking all are numbers or not
num="123"
print(num.isdigit()) #True
#checking all are alphabets or not
print(name.isalpha()) #True
print(num.isalpha()) #False
#checking all are lowercase or not 
print(name.islower()) #True
#checking all are uppercase or not
print(name.isupper()) # False

#chcking beginning or ending with
print(name.startswith("kh")) #True
print(name.endswith("ja"))#True








