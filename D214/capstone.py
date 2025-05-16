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

df.to_csv("cleaned_full_df.csv")
df = pd.read_csv("cleaned_full_df.csv")

print(df.dtypes)

import numpy as np
df['has owner answer'] = np.where(df["Owner Answer"] != "no answer", 1, 0)

print(df['has owner answer'])

#cleaning second df
df2 = pd.read_csv("new_data.csv")

#drop unneccesary features
df2 = df2.drop(columns=["spill1","spill2","spill3","spill4","spill5","spill6","spill7"])
print(df2.columns)

#data cleaning
num_missing_vals = df2.isna().sum()
print(num_missing_vals)

num_missing_reviews = df2['Review Text'].isna().sum()
print(num_missing_reviews)

df2 = df2.dropna(subset=['Review Text'])
print(df.columns)

num_missing_reviews = df2['Review Text'].isna().sum()
print(num_missing_reviews)

num_missing_replies = df2['Owner Answer'].isna().sum()
print(num_missing_replies)

df2['Owner Answer'] = df2["Owner Answer"].fillna('no answer')
num_missing_replies = df2['Owner Answer'].isna().sum()
print(num_missing_replies)

df2['Owner Answer Date'] = df2["Owner Answer Date"].fillna('no date')
num_missing_replies = df2['Owner Answer Date'].isna().sum()
print(num_missing_replies)

df2['Author'] = df2["Author"].fillna('anonymous')
num_missing_replies = df2['Author'].isna().sum()
print(num_missing_replies)

num_missing_vals = df2.isna().sum()
print(num_missing_vals)

df2.to_csv("cleaned_full_df2.csv")

df = pd.read_csv("cleaned_full_df.csv")
df2 = pd.read_csv("cleaned_full_df2.csv")

print(df.dtypes)
print(df2.dtypes)

import numpy as np
df['has owner answer'] = np.where(df["Owner Answer"] != "no answer", 1, 0)
df2['has owner answer'] = np.where(df2["Owner Answer"] != "no answer", 1, 0)

print(df['has owner answer'])
print(df2['has owner answer'])

import matplotlib.pyplot as plt

print(df['state'].unique())
print(df['state'].value_counts())
df.replace('Lousiana','Louisiana',inplace=True)
print(df['state'].unique())
print(df['state'].value_counts())

print(df2['state'].unique())
print(df2['state'].value_counts())

df = pd.concat([df,df2],ignore_index=True)

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

df = df.drop(columns='Unnamed: 0')
df = df.drop(columns='Unnamed: 0.1')
print(df.dtypes)

df['Author'] = df["Author"].replace({"#NAME?":"anonymous"})
num_missing_replies = df['Author'].isna().sum()
print(num_missing_replies)

def dupe_detection(column1, column2):
    dupes = df.duplicated(subset = column1, keep = False)
    duped_reviews = df[dupes].sort_values(by = column1)
    print(duped_reviews[[column1,column2]])

dupe_detection('Review Text','Author Profile')
df = df.drop_duplicates(subset=['Review Text'])
dupe_detection('Review Text','Author Profile')

df.to_csv("cleaned_full_df_with_census_regions.csv")

x = df['label']
plt.hist(x)
plt.xlabel('label')
plt.show()

print(df['census region'].value_counts())

def census_review_counts(region):
    count1 = df[(df['census region'] == region) & (df['label'] == 'positive')]
    count2 = df[(df['census region'] == region) & (df['label'] == 'negative')]
    count3 = df[(df['census region'] == region) & (df['label'] == 'neutral')]
    print(count1['label'].value_counts())
    print(count2['label'].value_counts())
    print(count3['label'].value_counts())

census_review_counts('southern') # 47476 pos | 33369 neg | 2631 neutral | 83476 total
census_review_counts('west') # 31535 pos | 18391 neg | 1557 neutral | 54183 total

import scipy.stats as stats
alpha = 0.05

observed = np.array([
    [47476, 33369, 2631],
    [31535, 18391, 1557]
])

chi2, p_value, degrees_of_freedom, expected_values = stats.chi2_contingency(observed)
print(expected_values)
print(p_value)