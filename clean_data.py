""" In this file we clean the data from the csv file and save it to a new csv file """

import pandas as pd
from bidi.algorithm import get_display

# read the csv file
df = pd.read_csv("data/table.csv")

# Split the 'שעות חדר' column into two new columns - 'חדר' and 'שעות'
df[["חדר", "שעות"]] = df["שעות חדר"].str.split(" ", n=1, expand=True)


# List of columns to drop (not needed)
columns_to_drop = ["של", "מכסה", "בפעל", "בהמתנה", "שעות חדר"]
# Drop the columns
df = df.drop(columns=columns_to_drop)


# List of column names in the order you want them to appear
column_order = ['נ"ז', "סמס", "חדר", "שעות", "יום", "מורה", "שם שעור"]
# Reorder the columns
df = df[column_order]


df.to_csv("data/clean_data.csv", index=False, encoding="utf-8")


# for display in Hebrew

# Reverse the rows
for col in df.select_dtypes(include=[object]):
    df[col] = df[col].apply(lambda x: get_display(str(x)) if pd.notnull(x) else x)

# # Reverse the column headers
# df.columns = [get_display(col) for col in df.columns]

df.to_csv("data/clean_data_revers.csv", index=False, encoding="utf-8")