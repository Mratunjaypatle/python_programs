# nested if 

"""
means putting one if statement inside another if statement  
"""

"""
Suppose a student can attend an exam 
if :
      student attendance should be more than 75 % 
      student fees should be paid 
"""
attendance = 73 
fees_paid = False 

if attendance >= 75 :
    if fees_paid  : 
       print("Student is eleigble for exam .. ")
    else :
       print("please pay your fees")
else :
   print("attend is too low , talk to your HOD")



