student={
    "name":"khadeeja",
    "age": 22,
    "course":"MCA"
}
print(student) #{'name': 'khadeeja', 'age': 22, 'course': 'MCA'}
print(student['name']) #khadeeja

# to return the values
print(student.values()) #dict_values(['khadeeja', 22, 'MCA'])

#now i dont have to take the keys instead print it by values is possible
for x in student.values():  #khadeeja 22 MCA
    print(x)


#whether a key is present
print("name" in student) #True

# if more than one students : inside list we use dictionary
student=[
    {
        "name":"faris",
        "age":19,
    },
    {
       "name":"navas",
        "age":45, 
    }
]
# To access the first student
print(student[0])  #{'name': 'faris', 'age': 19}
print(student)#[{'name': 'faris', 'age': 19}, {'name': 'navas', 'age': 45}]
print(student[0]['name']) #faris

# we can also access usig get method
print(student[1].get("name")) #navas

#change the value of studnet
student[1]['name']='ram'
print(student[1].get('name'))

#length
print(len(student)) #2

#assign another key value pair
student[0]["marks"]=40
print(student) #[{'name': 'faris', 'age': 19, 'marks': 40}, {'name': 'ram', 'age': 45}]

#to remove
student[0].pop("marks")
print(student) #[{'name': 'faris', 'age': 19}, {'name': 'ram', 'age': 45}]

# to clear
student.clear()
print(student)

#nesting of dictionary
test={
    "element1":{
        "item1":"value",
        "item2":"value"
    },
    "element2":{
        "item3":"value",
        "item4":{
            "item5":"value"
        }
    }
}
print(test)  #{'element1': {'item1': 'value', 'item2': 'value'}, 'element2': {'item3': 'value', 'item4': {'item5': 'value'}}}