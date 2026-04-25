#importing libraries
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt  
import seaborn as sns  
import statistics as stats

# import dataset
data = pd.read_csv('Titanic Dataset.csv')

data.head()

# mean value of age and fare

# mean value of age
mean_age = np.mean(data['Age'])
print("mean age of passengers is - ", mean_age)

# mean value of fare
mean_fare = np.mean(data['Fare'])
print("mean fare is - ", mean_fare)

# median value of age and fare 

median_age = np.median(data['Age'])
print("meadian value of age - ", median_age)

median_fare = np.median(data['Fare'])
print("median value of fare - ", mean_fare)

# mode value of age and pclass

mode_age = stats.mode(data['Age'])
print("mode value of age - ", mode_age)

mode_class = stats.mode(data['Pclass'])
print("mode value of PClass - ", mode_class)

# mode value of categorical feature - gender
mode_gender = data['Gender'].value_counts().index[0]
print("mode of feature gender - ", mode_gender)