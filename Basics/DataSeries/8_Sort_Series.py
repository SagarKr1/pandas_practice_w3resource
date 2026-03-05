# Write a Pandas program to sort a given Series.

import pandas as pd

ds= pd.Series(['100', '200', 'python', '300.12', '400'])

print(f"Data Series : \n{ds}\n")

ds = ds.sort_values()

print(f"Sorted Data Series : \n{ds}\n")
