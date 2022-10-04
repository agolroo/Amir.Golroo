import numpy as np
import pandas as pd

# LOAD THE DATA
df = pd.read_csv("Set1.CSV", header=0)
print(df.shape)

# EXPLORE THE DATA
print(df.head(5))
print(df.tail(5))
print("Number of participants:", df.shape[0] // 9) # 9 is the number of tasks per pid
print(df.iloc[660:670, :])

# MISSING DATA
print(df["duration"].value_counts() ["?"])

# ways to handle missing values
# 1. Discard them
# 2. Fill them (how?) --------- a. with the most frequent label / b. with central tendency measure / c. replace the "?" with np.NaN
# 3. Do nothing! 

df.replace("?", np.NaN, inplace=True)
print(df.isnull().sum())
df.dropna(inplace=True)
print("After Droping:", df.isnull().sum())
print(df.shape)
df.reset_index(inplace=True, drop=True)
print(df.head(2))

# DECODE TASK
# Replace 1-8 & dot with more human readable/meaningful labels
task_decoder = {"1": "Water Plants", "2": "Fill Medication Dispenser", "3": "Wash Countertop", "4": "Sweep & Dust", "5": "Cook", "6": "Wash Hands", "7": "Perform TUG", "8": "Perform TUG w/ Questions", "dot": "Day Out Task"}
def decode_task(df):
    ser = df["task"]
    for key in task_decoder:
        ser.replace(key, task_decoder[key], inplace=True)
decode_task(df)
print(df.head(10))

# CLEAN CLASS
def clean_class(df):
    ser = df["class"].copy()
    for i in range(len(ser)):
        curr_class = str(ser.iloc[i])
        curr_class = curr_class.lower()
        if "hoa" in curr_class or "healthy" in curr_class:
            ser.iloc[i] = "HOA"
        elif "pd" in curr_class or "parkinson" in curr_class:
            ser.iloc[i] = "PD"
        else:
            print("unrecognized status: %d, %s" %(i, curr_class))
   df["class"] = ser
   
clean_class(df)
print(df.head(25))
print(df["class"].value_counts())

# CHECK COLUMN TYPES
for column in df.columns:
    print(column, df[column].dtype)
    
print(type(df["duration"].sum()))  #logic error! duration vals are stored as strings
df["duration"] = df["duration"].astype(np.int32)
for column in df.columns:
    print(column, df[column].dtype)
print(type(df["duration"].sum()))
print(df["duration"].sum(), df["duration"].mean(), df["duration"].std())

# WRITE OUT THE CLEANED DATA
df.to_CSV("Set1_Cleaned.CSV", index=False)