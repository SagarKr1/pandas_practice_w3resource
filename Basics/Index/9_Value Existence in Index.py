# Write a Pandas program to check if a specified value exists in single and multiple column index dataframe.

import pandas as pd

df = pd.DataFrame(
    {
        "school_code": ["s001", "s002", "s003", "s001", "s002", "s004"],
        "class": ["V", "V", "VI", "VI", "V", "VI"],
        "name": [
            "Alberto Franco",
            "Gino Mcneill",
            "Ryan Parkes",
            "Eesha Hinton",
            "Gino Mcneill",
            "David Parkes",
        ],
        "date_Of_Birth": [
            "15/05/2002",
            "17/05/2002",
            "16/02/1999",
            "25/09/1998",
            "11/05/2002",
            "15/09/1997",
        ],
        "weight": [35, 32, 33, 30, 31, 32],
        "address": ["street1", "street2", "street3", "street1", "street2", "street4"],
        "t_id": ["t1", "t2", "t3", "t4", "t5", "t6"],
    }
)

df.set_index('t_id',inplace=True)

print(f"Original DataFrame:\n {df}\n")

print("t4" in df.index)
print("t11" in df.index)
df.reset_index(inplace=True)

df.set_index(['t_id',"class",'school_code'],inplace=True)

print(f"New Data Frame : \n{df}\n")

print('V' in df.index.levels[1])
print('s001' in df.index.levels[2])