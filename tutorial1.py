from pandas import DataFrame, read_csv

# General syntax to import a library but no functions: 
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

# Enable inline plotting
%matplotlib notebook

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

BabyDataset = list(zip(names,births))

df = pd.DataFrame(data=BabyDataset, columns = ['Names','Births'])

df.to_csv('birth1880.csv', index = False, header = False)

location = r'C:\Users\Flash\Downloads\Compressed\birth1880.csv'
df = pd.read_csv(location, header=None, names=['Names','Births'])

Sorted = df.sort_values(['Births'], ascending=False)
Sorted.head()

df['Births'].plot()
MaxValue = df['Births'].max()
MaxName = df['Names'][df['Births'] == df['Births'].max()].values
Text = str(MaxValue)+" - "+str(MaxName)
plt.annotate(Text, xy=(1,MaxValue), xytext = (8,0), xycoords = ('axes fraction','data'), textcoords = 'offset points')
print("The most popular name")
df[df['Births']==df['Births'].max()]