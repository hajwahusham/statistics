# importing libraries
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as sns 

# import dataset
data = pd.read_csv('Titanic Dataset.csv')

data.head(5)

# set plot style
sns.set_style('whitegrid')

# countplot for feature survived
sns.countplot(x='Survived', data=data)

# bar chart for showing passengers belonging to different gender who survived or not
sns.countplot(x='Gender', hue='Survived', data=data)

# customize plots
sns.countplot(x='Survived', data=data, palette='winter')

sns.countplot(x='Gender', hue='Survived', data=data, palette='winter')

# countplot for embarked
sns.countplot(x='Embarked', data=data)

# rotate the value labels and modify their font size

sns.countplot(x='Embarked', data=data)
plt.xticks(rotation=30, fontsize=20)
plt.show()