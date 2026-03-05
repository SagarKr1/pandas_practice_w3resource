# Write a Pandas program to convert a dictionary to a Pandas series.

import pandas as pd

dis = {
    "name":"Sagar",
    "role":"Majdur",
    "Description":"Working as a labour"
}

ds = pd.Series(dis)

print(ds)