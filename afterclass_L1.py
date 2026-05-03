#importing libraries
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt  
import seaborn as sns  
import statistics as stats

# import dataset
data = pd.read_csv('Bestsellers with categories.csv')

data.head()
print("-------------------------------")

# check the quantitative and categorical features of the dataset
data.info()
print("-------------------------------")

# check if any values are null (and handle if there's any (but there aren't))
print(data.isnull().sum())
print("-------------------------------")

# find the mean, median, mode of;
# user rating
# mean
mean_u_rating = np.mean(data['User Rating'])
print("mean user rating is - ", mean_u_rating)

# median
median_u_rating = np.median(data['User Rating'])
print("median of user rating is - ", median_u_rating)

# mode
mode_u_rating = stats.mode(data['User Rating'])
print("mode user rating is - ", mode_u_rating)
print("-------------------------------")

# price
# mean
mean_u_price = np.mean(data['Price'])
print("mean price is - ", mean_u_price)

# median
median_u_price = np.median(data["Price"])
print("median price is - ", median_u_price)

# mode
mode_u_price = stats.mode(data["Price"])
print("mode price is - ", mode_u_price)
print("-------------------------------")

# reviews
# mean
mean_u_reviews = np.mean(data['Reviews'])
print("mean of reviews is - ", mean_u_reviews)

# median
median_u_reviews = np.median(data["Reviews"])
print("median of reviews is - ", median_u_reviews)

# mode
mode_u_reviews = stats.mode(data["Reviews"])
print("mode of reviews is - ", mode_u_reviews)
print("-------------------------------")