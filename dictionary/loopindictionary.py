student = {
    # key -> value 
    "name" : "Rahul" ,
    "age" : 23,
    "marks" : 90
}

for key in student :
    print(key)


for value in student.values():
    print(value)

for key,value in student.items():
    print(key , ":" , value)

#nested dictionaries 

students = {
    "student1" :  {
        "name" : "Rahul" ,
         "age" : 19 ,
         "marks" : 90
    },
    "student2" :  {
            "name" : "priya" ,
             "age" : 19,
             "marks" : 80
},
}

print(students["student1"]["name"])


employees = {

    "emp1" : {
        "empname" : "arun" ,
        "department" : "IT",
        "salary" : 90000
    },

 "emp2" : {
        "empname" : "Prity" ,
        "department" : "HR",
        "salary" : 95000
    },

}

print(employees["emp2"]["department"])
# HR 
