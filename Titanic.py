"""
Created on Mon Nov 26 21:56:34 2018

@author: howardsu666
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

train = pd.read_csv("/Users/howardsu666/Github/Data_analysis/Titanic/train.csv")
test = pd.read_csv("/Users/howardsu666/Github/Data_analysis/Titanic/test.csv")

# Test if there is blank in the data
    #print(train.info)

#show the info of the data (Max, Min, 95% etc.)
    #print(train.describe())
    #print(test.describe())

# Convert Train and Test, Reset the index
data = train.append(test, sort = True) # Default sort = False
data.reset_index(drop = True, inplace = True) # inplace == True, don't create new Obj

# plot for survived or not
sns.countplot(data['Survived'])
#plt.show()

# plot for comparing the survived count base on differert "Class"
sns.countplot(data['Pclass'], hue = data['Survived'])
#plt.show()
#Gender: Female survivals are way more than male
sns.countplot(data['Sex'], hue = data['Survived'])
#plt.show()
# Embarked: People who was from S harbor was more likely to die
sns.countplot(data['Embarked'], hue = data['Survived'])
#plt.show()

#!!!!!!!!!!!
howard = sns.FacetGrid(data, col = 'Survived')
# kde = Whether to plot a gaussian kernel densi ty estimate.
howard.map(sns.distplot, 'Age', bins = 70, kde = False)
#plt.show()

sarah = sns.FacetGrid(data, col = 'Survived')
sarah.map(sns.distplot, 'Fare', kde = False)
#plt.show()
data['Fare'].describe()

helen = sns.FacetGrid(data, col = 'Survived')
helen.map(sns.distplot, 'Parch', kde = False)
#plt.show()

hans = sns.FacetGrid(data, col = 'Survived')
hans.map(sns.distplot, 'SibSp', kde = False)
#plt.show()

# Combine Parch and SibSp to make analysis accurate
data['Family_Size'] = data['Parch'] + data['SibSp']
sam = sns.FacetGrid(data, col = 'Survived')
sam.map(sns.distplot, 'Family_Size', kde = False)
#plt.show()

#[1] == show the number 1 of the str after split
# expand = True, return DataFrame/MultiIndex expanding dimensionality.
# expand = False, return Series/Index, containing lists of strings.
data['Title'] = data['Name'].str.split(', ', expand = True)[1]
#print(data['Name'].str.split(', ', expand = True).head(3))
#print(data['Title'])

data['Title'] = data['Title'].str.split('. ', expand = True)[0]
#print(data['Title'])

    #show the category in the 'Title'
print(data['Title'].unique())









