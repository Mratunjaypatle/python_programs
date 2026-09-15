students = ["Rahul" , "Amit" , "Priya" , 123 , 'A' , True]

print(students)

#indexing -> starts with 0

Animals = ["Tiger" , "Lion" , "Panther" , "Leopard"]
#             0        1          2           3
Animals[0] = "White Tiger"
print(Animals[0])
print(Animals[-1])
print(Animals[-2])

#slicing the list 
numbers = [10,20,30,40] 
#           0  1  2  3
print(numbers)
print(numbers[1:4])
print(numbers[:3])

#methods 
"""
append 
insert 
extends 
remove
pop
"""

data = [2,5,1,3,9]
data.sort()
print(data)
data.reverse()
print(data)
