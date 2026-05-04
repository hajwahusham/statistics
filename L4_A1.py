# import libraries
import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns 

# import dataset
data = pd.read_csv('Titanic Dataset.csv')

data.head(5)

# check null values
data.dtypes

# nominal and ordinal categorical features

# nominal categorical variables
nominal_cat = ['Name', 'Ticket', 'Cabin']

# ordinal categorical variables
ordinal_cat = ['Embarked', 'Gender']

# median values of feature gender and embarked
data['Gender'].value_counts()

gender_categories = ['Female', 'Male']

data['Gender'] = pd.Categorical(data['Gender'], gender_categories, ordered=True)

median_index = np.median(data['Gender'].cat.codes)
median_gender = gender_categories[int(median_index)]
print(median_gender)

data['Embarked'].value_counts()

embarked_categories = ['S', 'C', 'Q']

data['Embarked'] = pd.Categorical(data['Embarked'], embarked_categories, ordered=True)

median_index = np.median(data['Embarked'].cat.codes)
median_embarked = embarked_categories[int(median_index)]
print(median_embarked)