# importing libraries
import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

# import dataset
data = pd.read_csv('Titanic Dataset.csv')

data.head(5)

# check for null values
data.isnull().sum()

# quartiles of feature age

age_q1 = np.quantile(data['Age'], 0.25)
age_q2 = np.quantile(data['Age'], 0.50)
age_q3 = np.quantile(data['Age'], 0.75)

print("age quartiles :- ")
print("Q1 ", age_q1)
print("Q2 ", age_q2)
print("Q3 ", age_q3)

# interquartile range of feature Age

IQR_age = age_q3 - age_q1
print("interquartile range:- ", IQR_age)

# plot histogram for feature Age
plt.hist(data["Age"])
plt.ylabel("count of passengers")
plt.xlabel("age")
plt.show()

# qurtiles for feature fare

fare_q1 = np.quantile(data['Fare'], 0.25)
fare_q2 = np.quantile(data["Fare"], 0.50)
fare_q3 = np.quantile(data["Fare"], 0.75)

print("fare quartiles")
print("q1 ", fare_q1)
print("q2 ", fare_q2)
print("q3 ", fare_q3)

# interquartile range of feature Fare
IQR_fare = fare_q3 - fare_q1
print("interquartile range:- ", IQR_fare)

# plot histogram for feature Age
bins = np.arange(1, 250, 20)
plt.hist(data["Fare"], bins=np.arange(1, 250, 20))
plt.ylabel("countof passengers")
plt.xlabel("fare")
plt.xticks(bins)
plt.show()
