#Titanic Survival Prediction.

#Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


#Reading the csv file into a variable
titanic = pd.read_csv("./train_and_test2.csv")

#Viewing the 1st five rows
titanic.head()

#Viewing the last 5 rows
titanic.tail()

#Getting more info about the rows
titanic.info()

