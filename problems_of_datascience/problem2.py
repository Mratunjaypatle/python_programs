responses = ["Yes" , "No" ,"Yes" , "No","Yes" , "No","Yes" , "No","No" , "Yes" ]

frequency = {}
 
for response in responses :
    # yes 
    if response in frequency :
        frequency[response] += 1 
    else :
        frequency[response] = 1

print(frequency)


# student data analysis using dictionary 

student = {
    "name" : "Praveen",
    "age" : 23 ,
    "marks" : [78,79,89,90,99]
 }

marks = student["marks"]
total = sum(marks)
average = sum(marks) / len(marks)

print("Student : " , student["name"])
print("Age : " , student["age"])
print("Marks : " , student["marks"])
print("Total : " , total)
print("Average : " , average)


students =  [
     {"name" : "Vijay" , "marks" : 75},  
     {"name" : "Neha" , "marks" : 85},
     {"name" : "Ravi" , "marks" : 98},
     {"name" : "Priyanshu" , "marks" : 87},
     {"name" : "Bhavna" , "marks" : 78},
]

for data_student in students :
    print(data_student["name"] ,  ":" , data_student["marks"])

top_mark = student[0]
# A B C D E 