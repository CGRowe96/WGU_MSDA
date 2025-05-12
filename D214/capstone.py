import os
import pandas as pd

directory = os.chdir("G:\My Drive\Capstone Files\Datasets")

#load and print csv index
df = pd.read_csv("full.csv")
print(df.columns)

#drop unneccesary features
df = df.drop(columns=["spill1","spill2","spill3","spill4","spill5","spill7","spill7.1","spill8"])
print(df.columns)

#data cleaning
num_missing_vals = df.isna().sum()
print(num_missing_vals)

num_missing_reviews = df['Review Text'].isna().sum()
print(num_missing_reviews)

df = df.dropna(subset=['Review Text'])
print(df.columns)

num_missing_reviews = df['Review Text'].isna().sum()
print(num_missing_reviews)

num_missing_replies = df['Owner Answer'].isna().sum()
print(num_missing_replies)

df['Owner Answer'] = df["Owner Answer"].fillna('no answer')
num_missing_replies = df['Owner Answer'].isna().sum()
print(num_missing_replies)

df['Owner Answer Date'] = df["Owner Answer Date"].fillna('no date')
num_missing_replies = df['Owner Answer Date'].isna().sum()
print(num_missing_replies)

df['Author'] = df["Author"].fillna('anonymous')
num_missing_replies = df['Author'].isna().sum()
print(num_missing_replies)

num_missing_vals = df.isna().sum()
print(num_missing_vals)

#df.to_csv("cleaned_full_df.csv")

df = pd.read_csv("cleaned_full_df.csv")

print(df.dtypes)

import numpy as np
df['has owner answer'] = np.where(df["Owner Answer"] != "no answer", 1, 0)

print(df['has owner answer'])

import matplotlib.pyplot as plt

x = df['label']
plt.hist(x)
plt.xlabel('label')
plt.show()

print(df['state'].unique())
print(df['state'].value_counts())
df.replace('Lousiana','Louisiana',inplace=True)
print(df['state'].unique())
print(df['state'].value_counts())

df['census region'] = np.where((df['state'] == 'Maine')|(df['state'] == 'New Hampshire')|(df['state'] == 'Vermont')|(df['state'] == 'Massachusetts')|
                              (df['state'] == 'Connecticut')|(df['state'] == 'Rhode Island')|(df['state'] == 'New York')|(df['state'] == 'Pennsylvania')|
                              (df['state'] == 'New Jersey'),'northeast',np.where((df['state'] == 'Delaware')|(df['state'] == 'Maryland')|(df['state'] == 'District of Columbia')|
                              (df['state'] == 'Virginia')|(df['state'] == 'West Virginia')|(df['state'] == 'Kentucky')|(df['state'] == 'Tennessee')|(df['state'] == 'North Carolina')|
                              (df['state'] == 'South Carolina')|(df['state'] == 'Georgia')|(df['state'] == 'Florida')|(df['state'] == 'Alabama')|(df['state'] == 'Mississippi')|
                              (df['state'] == 'Louisiana')|(df['state'] == 'Oklahoma')|(df['state'] == 'Arkansas')|(df['state'] == 'Texas'),'southern',
                              np.where((df['state'] == 'Michigan')|(df['state'] == 'Ohio')|(df['state'] == 'Indiana')|(df['state'] == 'Illinois')|(df['state'] == 'Wisconsin')|
                              (df['state'] == 'Missouri')|(df['state'] == 'Iowa')|(df['state'] == 'Minnesota')|(df['state'] == 'North Dakota')|(df['state'] == 'South Dakota')|
                              (df['state'] == 'Nebraska')|(df['state'] == 'Kansas'),'midwest',np.where((df['state'] == 'Montana')|(df['state'] == 'Wyoming')|(df['state'] == 'Colorado')|
                              (df['state'] == 'New Mexico')|(df['state'] == 'Arizona')|(df['state'] == 'Utah')|(df['state'] == 'Idaho')|(df['state'] == 'Nevada')|(df['state'] == 'Washington')|
                              (df['state'] == 'Oregon')|(df['state'] == 'California')|(df['state'] == 'Alaska')|(df['state'] == 'Hawaii'),'west','?'))))

print(df['census region'].value_counts())