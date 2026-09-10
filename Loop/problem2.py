# 4. Print the multiplication table of a number entered by the user.

num = int(input("enter a number   ")) # 12

for i in range (1 , 11) :
    result = num * i 
    print(f"{num} * {i} = {result}") # 12 24 36   120 

