# Logical operators are used to combine multiple conditions
# and or not 
age = 20
print(age > 18 and  age < 18) 
        # True and  False
        # 1    and   0  => 0
print(age > 50 and age < 19)
    # false and false -> false
print(age > 50 and age > 19)    
     # false and true  -> false
print(age>10 and age < 50)
     # true and true  -> True

print("conditions checked for virat score..")
virat_score = 183

print(virat_score > 200 or virat_score < 100)
    # false and false -> false
print(virat_score > 200 or virat_score > 100) 
    # true
print(virat_score < 100 or virat_score > 100)
    # true
print(virat_score > 100 or virat_score < 200)

x = 10
y = 20
z = x > y # false
print("The value of z is " , not z)
# false -> true 
# true -> false 
