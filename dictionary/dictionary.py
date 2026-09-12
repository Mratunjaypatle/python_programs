students = {
    # key -> value 
    "name" : "Rahul" ,
    "age" : 23,
    "marks" : 90
}
# updation

students["age"] = 24
students["course"] = "Python"
print(students.get("age"))
print(students["name"])
print(students.get("salary")) # none

print(students)

#delete the element 

students.pop("age")
print(students) 
del students["marks"]
print(students)

students.clear()
print(students)

#methods 
"""
key()
value()
items()

"""