#importing libraries
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt  
import seaborn as sns  
import statistics as stats

# import dataset
data = pd.read_csv('Bestsellers with categories.csv')

# check if any values are null (and handle if there's any (but there aren't))
print(data.isnull().sum())
print("-------------------------------")

# find the varience and standard deviation of user rating
var_u_rating= np.var(data['User Rating'])
print("variation of User Rating is: ", var_u_rating)

standard_deviation_u_rating = np.std(data['User Rating'])
print("standard deviation of User Rating is: ", standard_deviation_u_rating)
print("-------------------------------")

# find the varience and standard deviation of price
var_price= np.var(data['Price'])
print("variation of price is: ", var_price)

standard_deviation_price = np.std(data['Price'])
print("standard deviation of price is: ", standard_deviation_price)
print("-------------------------------")
# check the distribution of user rating using a histogram
bins = np.arange(3, 5, 0.1)
plt.hist(data['User Rating'], bins=bins,)
plt.xlabel("rating")
plt.ylabel("no. of users")
plt.xticks(bins)
plt.show()

# check the distribution of price using a histogram
bins = np.arange(0, 117, 5)
plt.hist(data['Price'], bins=bins,)
plt.xlabel("price")
plt.ylabel("no. of books")
plt.xticks(bins)
plt.show()