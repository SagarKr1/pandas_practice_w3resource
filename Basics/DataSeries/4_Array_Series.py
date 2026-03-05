# Write a Pandas program to convert a NumPy array to a Pandas series.

import numpy as np
import pandas as pd

arr = np.arange(1,11)
ds = pd.Series(arr)
print(ds)