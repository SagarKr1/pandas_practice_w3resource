# Write a Pandas program to change the data type of given a column or a Series.

import pandas as pd
lst = [1,2,3,4,5]

ds = pd.Series(lst,dtype=float)

print(ds)