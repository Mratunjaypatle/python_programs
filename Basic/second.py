student = {

    "name" : "Shubham" ,
    # key :    value
    "age" : 20 ,
    "email" : "shubham@gmail.com",
    "is_login" : True
}

print(student["name"])
print(student["is_login"])
print(student["is_login"])
print(student["age"])

#list -> it is an ordered collection os items , mutable .

employee = ["Rahul" , "Amit" , "Priya"]
employee[0] = "Adam"
# pre defined function of list
employee.append("Aditya")
employee.extend(["manish" , "sumit"])
employee.remove("Amit")
employee.insert(1 , "sumit")
employee.pop(2)

print(employee)

numbers = [1,2,5,3,8,7]

# pre defined function of python
print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))


# Set -> set is unordered collection of unique elements 

number = {10 , 20 , 30 , 40}
# preddefined function in set
number.add(50)
number.update([10 , 100])
number.remove(100)
# print(number)

A = {1,2,3,4}
B = {4,5,6}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))

print(A.issubset(B))
# checks whether all elements of A are present in B 
print(A.issuperset(B))
# checks whethere all elements of B are present in A

print(A.isdisjoint(B))
# checks whether A and B have no common elements

