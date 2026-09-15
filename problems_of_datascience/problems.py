# Find students above average

marks = [45 , 78 , 90 , 56 , 88 , 34 , 70]

average = sum(marks) / len(marks)

print("Average is " , average)

print("Students above average")

for mark in marks :
    if mark > average :
        print(mark)

# find all even and odd values in a dataset

data = [12,25,15,56,78,90,80,86,87,45]

even_numbers = []
odd_numbers = []

for number in data :
    if number % 2 == 0 :
        even_numbers.append(number)
    else :
        odd_numbers.append(number)

print("even values are " , even_numbers)
print("odd values are " , odd_numbers)


