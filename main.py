import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Loading the dataset
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
#print(train.head())
#print(test.head())

#print(train.info())
print(train.describe)