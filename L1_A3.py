#importing libraries
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt  
import seaborn as sns  

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
