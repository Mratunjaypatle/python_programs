"""
Loop -> it is used when we want to execute the same block of code repeatedly ..
there are some types of loop in python
for loop
while loop 
"""

 

for i in range(2) :
    print("hello world")


# print even numbers 

for i in range (2 , 21 , 2 ) :
    print(i)
# 2 3 4 5 6 7 8 9 10 20 


# print numbers in reverse 

for i in range(10 , 0 , -1 ) :
    print(i)


#  10 to 1
"""
for loop => We want to iterate over a sequence or collection . such as string , tuple , List

"""

# for variable in sequence 

# stop and step - 1 
# for i in range(1 , 11) :
#     print(i)

# for j in range(5 , 0 , -3 ) :
#     print(j)


# range(stop)
# range(start , stop)
# range(start , stop , step)

# 1 2 3 4 5 
# step 2-1 => 1

name = "Robert John"

for character in name :
    print(character)


# we want to count the character in the string 
string = "python "
count = 0

for character in string :
    count = count + 1

print("numbers of character :" , count)


fruits = ["apple" , "banana" , "Mango"]

for name_of_fruits in fruits :
    print(name_of_fruits)

marks = [10,20,30]
for mark in marks :
    print(mark)