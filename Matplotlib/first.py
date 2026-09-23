# plot 
import matplotlib.pyplot as plt
x = [1,2,3,4,5] # months
y = [10000,12000,30000,45000 , 90000] # revenue
plt.title("Bussiness Analysis")
plt.xlabel("months") 
plt.ylabel("revenue")
plt.plot(x,y)
plt.grid(True)
plt.show()




import matplotlib.pyplot as plt
import pandas as pd

data_sales = {
      "Months" : ["Jan" , "Feb" , "March" , "April" , "May"] ,
      "Sales" : [100 , 120 , 150 , 130 , 180]
}
df_sales = pd.DataFrame(data_sales)
plt.plot(data_sales["Months"] , data_sales["Sales"] , marker = "o")
plt.grid(True)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("sales")
plt.show()



import matplotlib.pyplot as plt
import pandas as pd

data = {
    "salary" : [25000 , 80000 , 67000 , 56000 , 45000,55000]
}
data_frame = pd.DataFrame(data)
print(data_frame)

plt.plot(data["salary"] , color = "green" , marker = "o" , linestyle = "--")
plt.grid()
plt.show()

# print(data["salary"])

# histogram

import matplotlib.pyplot as plt
marks = [45, 50, 55, 60, 62, 76, 87, 78, 67, 56, 54, 50, 89, 90, 99, 98, 97, 96, 65, 78, 84 , 98]
plt.hist(marks)
plt.title("Distribution of marks")
plt.xlabel("Marks")
plt.ylabel("Student")

plt.show()

# scatter plot -> build relationship btw two variables

import matplotlib.pyplot as plt
mango_quantities = [1,2,3,4,5,6]
mango_prices = [40 , 60 , 80 , 100 , 140 , 200]

plt.scatter(mango_quantities , mango_prices)

plt.title("Mango Price vs Quantities ")
plt.xlabel("Mango Quantities")
plt.ylabel("Mango Prices")

plt.show()

# bar chart -> for comparing two things categorically 

import matplotlib.pyplot as plt
countries = ["USA" , "China" , "Germany" , "Japan" , "Unites Kingdom"]
economies = [32.38 , 20.85 ,5.45 , 4.38 , 4.26]
plt.bar(countries , economies)
plt.title("Economies")
plt.xlabel("Countries")
plt.ylabel("Economies")

plt.show()

# pie chart - it shows parts of a whole