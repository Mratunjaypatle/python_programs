#Write a program to check whether a number is positive, negative, or zero. 
# positive greater than 0  1 2 3 
# negative means less than 0 -2 -3 -4 

num = int(input("enter the number  ")) # 12

if num > 0 :
    print("positive number..")
elif num < 0 :
    print("negative number")
else :
    print("Zero ")

# Write a program to find the largest of three numbers.

num1 = 12 
num2 = 25
num3 = 100

if num1>num2 and num1>num3 :
    largest = num1 
elif num2>num1 and num2>num3 :
    largest = num2 
else :
    largest = num3

print("largest number is " , largest)

result = max(num1 , num2 , num3)
print("Result is " , result)

#Find the sum of numbers from 1 to 100.

total_sum = sum(range(1,101)) 
print(total_sum)

# using while loop 

total_sum_again = 0 
number = 1

while number <= 100 :
     total_sum_again = total_sum_again + number # 15
     number = number +  1 # 101


print( " total sum of 1 to 100 is "  , total_sum_again)

# 4. Print the multiplication table of a number entered by the user.

