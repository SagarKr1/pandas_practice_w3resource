# Write a Pandas program to get the items of a given series not present in another given series.

import pandas as pd

ds1 = pd.Series([1,2,3,4,5,6])
ds2 = pd.Series([1,7,3,9,5,8])

dif =ds1[ ~ds1.isin(ds2)]

print(dif)
