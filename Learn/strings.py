#strings
str1="welcome" 
str2='kaija' 
str3=40
print(str1) #welcome
print(str2) #welcome

#consider string as array
print(str1[0]) # w

#concatenate
print(str1+ str2) #welcomekaija
print("hello" "world") #hello world
print("hello" +str2) #hellokaija

 #we can't concatenate a string with a number . So we convert it into string
print("hello" + str(str3)) #hello40

# find substring 
s1="khadeeja beevi"
s2=25
print(s1[0:2]) # kh
print(s1[3:])  # deeja beevi
print(s1[3:5]) # de
print(s1[-1:]) #i

#reverse a string
print(s1[::-1]) # iveeb ajeedahk

# multiline string
s3="""hai its me 
kaija how are you?
have you had your food?
"""
print(s3)

# length of the string
print(len(s1))