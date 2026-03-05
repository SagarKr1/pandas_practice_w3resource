# Write a Pandas program to add some data to an existing Series.

import pandas as pd

ds = pd.Series([1,2,3,4,5])

print(f"Original series : {ds}\n")

lst = [6,7,8,9]

ds = pd.concat([ds,pd.Series(lst)],ignore_index=True)
print(ds)