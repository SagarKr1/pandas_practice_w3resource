# Write a Pandas program to create a subset of a given series based on value and condition.

import pandas as pd

ds = pd.Series([1,2,3,4,5,6,7,8,9,10])

print(f"Original series : {ds}\n")

newSeries = ds[ds<=5]

print(newSeries)