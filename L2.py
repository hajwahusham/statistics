# import libraries

import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt  
import seaborn as sns  

# import dataset

data = pd.read_csv('Weather Dataset.csv')

data.head(5)

data.info()

# check null values

data.isnull().sum()

# no feature has null values
# mean, varience and standard deviation of temperature (C)

mean_temp = np.mean(data['Temperature (C)'])
print("mean temperature is: ", mean_temp)

var_temp= np.var(data['Temperature (C)'])
print("variation of temperature is: ", var_temp)

standard_deviation_temp = np.std(data['Temperature (C)'])
print("standard deviation of temperature is: ", standard_deviation_temp)

#  mean, varience and standard deviation of temperature (C) for every month

for i in range(1,13):
    month = data.loc[data["month"] == i]['Temperature (C)']
    print("for month"+str(i))
    print("mean temperature is"+ str(np.mean(month)))
    print("standard deviation is"+ str(np.std(month))+ "\n")