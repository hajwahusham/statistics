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

# find the value that devides 10% of data for price
quantile10 = np.quantile(data['Price'], 0.10)
print(quantile10)
print("-------------------------------")

# quartiles of feature price
price_q1 = np.quantile(data['Price'], 0.25)
price_q2 = np.quantile(data['Price'], 0.50)
price_q3 = np.quantile(data['Price'], 0.75)

print("Price quartiles :- ")
print("Q1 ", price_q1)
print("Q2 ", price_q2)
print("Q3 ", price_q3)

# interquartile range of price

IQR_price = price_q3 - price_q1
print("interquartile range:- ", IQR_price)
print("-------------------------------")

# quartiles of feature user rating
u_rating_q1 = np.quantile(data['User Rating'], 0.25)
u_rating_q2 = np.quantile(data['User Rating'], 0.50)
u_rating_q3 = np.quantile(data['User Rating'], 0.75)

print("user ratings quartiles :- ")
print("Q1 ", u_rating_q1)
print("Q2 ", u_rating_q2)
print("Q3 ", u_rating_q3)

# interquartile range of u_ratings

IQR_u_rating = u_rating_q3 - u_rating_q1
print("interquartile range:- ", IQR_u_rating)

# box plot
# Price
plt.boxplot(data['Price'], vert=False)
plt.xlabel('Price')
plt.show()

# User Rating
plt.boxplot(data['User Rating'], vert=False)
plt.title('Boxplot of User Rating')
plt.xlabel('Rating')
plt.show()