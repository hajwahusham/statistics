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