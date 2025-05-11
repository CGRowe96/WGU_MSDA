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