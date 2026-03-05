# Write a Pandas program to append a new row 'k' to data frame with given values for each column. 
# Now delete the new row and return the original DataFrame.

# Sample Python dictionary data and list labels:
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
# 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
# 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
# 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# Values for each column will be:
# name : "Suresh", score: 15.5, attempts: 1, qualify: "yes", label: "k"

import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
df = pd.DataFrame(exam_data,index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

print(f"Orignal Data frame : \n {df}\n")

df.loc['k'] = ['Suresh',15.5,1 ,'yes']

print(f"New Data Added : \n{df}\n")

df = df.drop('k')

print(df)