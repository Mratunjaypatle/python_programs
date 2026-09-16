#External library 
import pandas as pd 
#Data Frame

data = {
    "Name" : ["Rahul" , "Virat" , "Rohit"] ,
    "age" : [23,21,24] ,
    "Salary" : [10000 , 23000 , 43000],
    "city" : ["Mumbai" , "Banglore" , "Indore"]
}
 
data_frame = pd.DataFrame(data)


print(data_frame)

# Tell me which employe earns most..

print("lowest salary is " , data_frame["Salary"].min())