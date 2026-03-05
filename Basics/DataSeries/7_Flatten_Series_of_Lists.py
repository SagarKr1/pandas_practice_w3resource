# Write a Pandas program to convert Series of lists to one Series.

import pandas as pd

ds = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']])

print(f"Data Series : \n {ds}\n")

ds = pd.Series([item for sublist in ds for item in sublist])

print(ds)