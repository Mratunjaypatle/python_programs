# even or odd number 
# even number -> divided by 2  2, 4 , 6 , 8
# odd number -> not divided by 2 -> 3,5,7,9

number = int(input("Enter the number =>  "))
# 12 
    # 12 % 2 => 0 

if number % 2 == 0 :
   print("Even number")
else :
   print("odd number ")


# database
data_name = "Admin"
data_password = "1234"

username = input("Enter the username ")
password = input("Enter the password ")

if username == data_name and password == data_password :
    #   false    and   true  -> false
   print("user login successfully")
else :
   print("user login unsuccessfully")


# if elif else
# making student grade result 
"""
90 or above  -> A
75 - 89 -> B
60 - 74 -> C
40 -59 -> D 
below than 40 -> fail
"""

student_marks = 90

if  student_marks >= 90  :
   print("Grade A") 
elif student_marks >= 75 :
   print("Grade B")
elif student_marks >= 60 :
   print("Grade C")
elif student_marks >= 40 :
   print("Grade D")
else :
   print("Fail")

