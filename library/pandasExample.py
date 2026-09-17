import pandas as pd
"""
Series (one column)
DataFrame (Table)
"""


marks = pd.Series([85,78,67,79,90])
print(marks)
print(marks[0])

studentsMarks = pd.Series(
    [85,78,67] ,
    index=["Vijay" , "Prity" , "Santosh"]
)
print(studentsMarks)

employe = pd.Series(
    ["Mumbai" , "Delhi" , "Indore" , "Vizag"],
    index=["Rahul" ,"Pranay"  , "Aayush" , "Vikki"]
                    )
            
print(employe)

CountryDetails = {
    "USA" : "Dollar $",
    "India" : "Rupees ₹",
} 
print(CountryDetails)
currencyDetails = pd.Series(CountryDetails) 
print(currencyDetails)

