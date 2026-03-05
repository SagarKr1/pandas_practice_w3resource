# Write a Pandas program to add, subtract, multiple and divide two Pandas Series.

import pandas as pd

ds1 = pd.Series([1,2,3,4,5])
ds2 = pd.Series([6,7,8,9,0])

print(f"Add : {ds1+ds2}\n")
print(f"Sub : {ds1-ds2}\n")
print(f"Multiply : {ds1*ds2}\n")
print(f"Divide : {ds1/ds2}\n")
