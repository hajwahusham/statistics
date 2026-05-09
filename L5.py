# importing libraries
import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt  
import seaborn as sns  

# importing the data set
data = pd.read_csv('Titanic Dataset.csv')

data.head(5)

# minimum and maximum values of age
minimum_age = data['Age'].min()
print("minimum age: ", minimum_age)

maximum_age = data['Age'].max()
print("maximum age: ", maximum_age)

# creating binned age and giving it a label
bins = [0, 15, 30, 45, 60, 75]

data['binned_age'] = pd.cut(data['Age'], bins)

print(data[['binned_age', 'Age']].head())

age_labels = ['Young', 'Young - Adult', 'Middle Aged', 'Middle-Older Age', 'Senior']

# bin the value of the age column and specify the labels
data['binned_age'] = pd.cut(data['Age'], bins, labels= age_labels)

# barplot for binned age
data['binned_age'].value_counts().plot(kind='bar')

# label the bar graph
plt.title('dance class age distribution')
plt.xlabel('ages')
plt.ylabel('count')
plt.show()

# conclusion
'''
- features gender and embarked have only 2 and 3 categories respectively
- other categorical features have too many categories to even collapse
'''
# cheack the distribution and skewness of all the features
labels = ['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
for label in labels:
    print('distributiion of ', label)
    sns.displot(data[label])
    plt.show()
    print('skewness - ', data[label].skew())

# conclusion

# log transform skewed features
data['log_SibSp'] = np.log(data['SibSp'])
data['log_Parch'] = np.log(data['Parch'])
data['log_Fare']  = np.log(data['Fare'])