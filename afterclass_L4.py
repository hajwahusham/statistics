#importing libraries
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt  
import seaborn as sns  
import statistics as stats
from sklearn.preprocessing import StandardScaler

# import dataset
data = pd.read_csv('Bestsellers with categories.csv')

# check if any values are null (and handle if there's any (but there aren't any))
print(data.isnull().sum())
print("-------------------------------")

# find the frequency of the categories for feature genre
print(data['Genre'].value_counts())
print("-------------------------------")

# finding the median
categories = ['Fiction', 'Non Fiction']
data['Genre'] = pd.Categorical(data['Genre'], categories, ordered=True)
median_index = np.median(data['Genre'].cat.codes)
median = categories[int(median_index)]
print("median of feature genre:- ", median)
print("-------------------------------")

# creating a bar chart feature genre
sns.countplot(x='Genre', hue='Genre', data=data, palette='YlOrRd')
plt.show()

# creating a pie chart feature genre
data.groupby('Genre', observed=True).size().plot(kind='pie', autopct='%.2f')
plt.show()

#Create new dataset with only numerical features
print(data.info())
# user rating reviews price year needed
num_data = data.drop(['Name', 'Author', 'Genre'], axis=1)

# check the spread of its features using a boxplot
for label in num_data.columns:
  plt.boxplot(num_data[label])
  print('Distribution of', label)
  plt.show()

# transform the data using normalisation or standardisation
scaler = StandardScaler()
num_data = scaler.fit_transform(num_data)
print(num_data)