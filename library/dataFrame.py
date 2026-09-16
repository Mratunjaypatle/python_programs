import pandas as pd

# data = {
#    "Name" : ["Angel" , "shaik" , "Shreya" , "Pavani"] ,
#    "Age" : [21,22,21,23],
#     "city" : ["kolkata" , "mumbai" , "delhi", "noida"]
# }

data = [
    {"Name": "Angel", "Age": 21, "City": "Kolkata", "Occupation": "Data Analyst", "Salary": 48000, "Active": True},
    {"Name": "Shaik", "Age": 24, "City": "Mumbai", "Occupation": "Software Engineer", "Salary": 65000, "Active": True},
    {"Name": "Pavani", "Age": 22, "City": "Noida", "Occupation": "UI/UX Designer", "Salary": 42000, "Active": False},
    {"Name": "Mratunjay", "Age": 22, "City": "Nagpur", "Occupation": "Backend Developer", "Salary": 50000, "Active": True},
    {"Name": "Aarav", "Age": 28, "Occupation": "DevOps Engineer", "Salary": 85000, "Active": True},
    {"Name": "Diya", "Age": 23, "City": "Pune", "Occupation": "Marketing Executive", "Salary": 38000, "Active": True},
    {"Name": "Rohan", "Age": 26, "City": "Hyderabad", "Occupation": "Full Stack Developer", "Salary": 72000, "Active": False},
    {"Name": "Ananya", "Age": 25, "City": "Delhi", "Occupation": "Product Designer", "Salary": 58000, "Active": True},
    {"Name": "Vikram", "Age": 30, "City": "Chennai", "Occupation": "Engineering Manager", "Salary": 115000, "Active": True},
    {"Name": "Pooja", "Age": 27, "City": "Jaipur", "Occupation": "Content Strategist", "Salary": 40000, "Active": False},
    {"Name": "Kabir", "Age": 29, "City": "Gurugram", "Occupation": "Product Manager", "Salary": 98000, "Active": True},
    {"Name": "Meera", "Age": 22, "City": "Ahmedabad", "Occupation": "Frontend Developer", "Salary": 45000, "Active": True},
    {"Name": "Siddharth", "Age": 31, "City": "Bengaluru", "Occupation": "Cloud Architect", "Salary": 130000, "Active": True},
    {"Name": "Sneha", "Age": 24, "City": "Kochi", "Occupation": "Quality Analyst", "Salary": 41000, "Active": True},
    {"Name": "Arjun", "Age": 27, "City": "Chandigarh", "Occupation": "Financial Analyst", "Salary": 62000, "Active": False},
    {"Name": "Isha", "Age": 23, "City": "Indore", "Occupation": "Graphic Designer", "Salary": 36000, "Active": True},
    {"Name": "Tanmay", "Age": 26, "City": "Bhopal", "Occupation": "Systems Admin", "Salary": 49000, "Active": True},
    {"Name": "Kavya", "Age": 25, "City": "Lucknow", "Occupation": "HR Specialist", "Salary": 44000, "Active": True},
    {"Name": "Aditya", "Age": 29, "City": "Mumbai", "Occupation": "Data Scientist", "Salary": 92000, "Active": False},
    {"Name": "Riya", "Age": 21, "City": "Kolkata", "Occupation": "Associate Researcher", "Salary": 35000, "Active": True},
    {"Name": "Nikhil", "Age": 28, "City": "Pune", "Occupation": "Cybersecurity Analyst", "Salary": 78000, "Active": True},
    {"Name": "Zoya", "Age": 24, "City": "Hyderabad", "Occupation": "Technical Writer", "Salary": 43000, "Active": True},
    {"Name": "Karan", "Age": 32, "City": "Delhi", "Occupation": "Operations Head", "Salary": 105000, "Active": False},
    {"Name": "Bhavna", "Age": 23, "City": "Surat", "Occupation": "Accountant", "Salary": 39000, "Active": True},
    {"Name": "Gaurav", "Age": 27, "City": "Bengaluru", "Occupation": "Mobile App Developer", "Salary": 69000, "Active": True},
    {"Name": "Nandini", "Age": 26, "City": "Chennai", "Occupation": "Business Analyst", "Salary": 59000, "Active": True},
    {"Name": "Farhan", "Age": 25, "City": "Patna", "Occupation": "Database Administrator", "Salary": 51000, "Active": False},
    {"Name": "Shreya", "Age": 22, "City": "Noida", "Occupation": "Social Media Lead", "Salary": 37000, "Active": True},
    {"Name": "Manish", "Age": 30, "City": "Vadodara", "Occupation": "Network Engineer", "Salary": 61000, "Active": True},
    {"Name": "Alia", "Age": 24, "City": "Mumbai", "Occupation": "SEO Specialist", "Salary": 46000, "Active": True},
    {"Name": "Pranav", "Age": 28, "City": "Coimbatore", "Occupation": "Machine Learning Engineer", "Salary": 88000, "Active": True},
    {"Name": "Ritika", "Age": 23, "City": "Visakhapatnam", "Occupation": "QA Tester", "Salary": 39000, "Active": False},
    {"Name": "Harsh", "Age": 26, "City": "Nagpur", "Occupation": "Site Reliability Engineer", "Salary": 74000, "Active": True},
    {"Name": "Tara", "Age": 25, "City": "Thiruvananthapuram", "Occupation": "UI Designer", "Salary": 47000, "Active": True},
    {"Name": "Varun", "Age": 29, "City": "Gurugram", "Occupation": "Scrum Master", "Salary": 82000, "Active": True},
    {"Name": "Simran", "Age": 22, "City": "Amritsar", "Occupation": "Talent Acquisition Associate", "Salary": 34000, "Active": False},
    {"Name": "Kunal", "Age": 31, "City": "Kolkata", "Occupation": "Solutions Architect", "Salary": 120000, "Active": True},
    {"Name": "Avani", "Age": 24, "City": "Dehradun", "Occupation": "Digital Marketer", "Salary": 41000, "Active": True},
    {"Name": "Yash", "Age": 27, "City": "Pune", "Occupation": "Automation Tester", "Salary": 55000, "Active": True},
    {"Name": "Deepika", "Age": 28, "City": "Hyderabad", "Occupation": "Project Coordinator", "Salary": 64000, "Active": False},
    {"Name": "Rahul", "Age": 25, "City": "Bengaluru", "Occupation": "Golang Developer", "Salary": 71000, "Active": True},
    {"Name": "Neha", "Age": 23, "City": "Ranchi", "Occupation": "Customer Success Specialist", "Salary": 36000, "Active": True},
    {"Name": "Abhishek", "Age": 33, "City": "Noida", "Occupation": "Technical Lead", "Salary": 112000, "Active": True},
    {"Name": "Swati", "Age": 26, "City": "Bhubaneswar", "Occupation": "Copywriter", "Salary": 42000, "Active": True},
    {"Name": "Mohit", "Age": 29, "City": "Jaipur", "Occupation": "Security Engineer", "Salary": 80000, "Active": False},
    {"Name": "Tanvi", "Age": 22, "City": "Guwahati", "Occupation": "Junior Analyst", "Salary": 35000, "Active": True},
    {"Name": "Sameer", "Age": 30, "City": "Mumbai", "Occupation": "Growth Manager", "Salary": 96000, "Active": True},
    {"Name": "Priyanka", "Age": 27, "City": "Delhi", "Occupation": "Compliance Officer", "Salary": 63000, "Active": True},
    {"Name": "Vivek", "Age": 28, "City": "Mysuru", "Occupation": "Data Engineer", "Salary": 77000, "Active": False},
    {"Name": "Anjali", "Age": 24, "City": "Kolkata", "Occupation": "Product Analyst", "Salary": 53000, "Active": True}
]

data_frame = pd.DataFrame(data)

# print(data_frame)

# print(data_frame.shape)
# print(data_frame.size)

# print(data_frame.dtypes)

# print()
print(data_frame["City"])
print(data_frame.head(15)) # provides first 5 data from dataset
print(data_frame.tail()) # provides last 5 data from dataset

print(data_frame.info()) 

# print(data_frame.describe())