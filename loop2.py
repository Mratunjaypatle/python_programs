# while loop -> a while loop repeatedly executes code as long as condition remains true 

# while condition :
#     code 

i = 1  # starting point 
while i<=10 :  
    print(i)  
    i = i+1 # stepping 


    
print("break and continue`")
# break and continue

for i in range(1 , 11) : 
     if i == 5 :
          break 
     print(i)

students = ["ram" , "shyam" , "ramesh" , "shivam" , "aniket"]

for student in students : 
     if student == "ramesh" :
          break 
     print(student)

#  continue in loop -> skip the current iteration and move to others
for i in range(1,6):
     if i == 3 :
          continue
     print(i)
     


for i in range(1,6) :
     pass

print("code completed")