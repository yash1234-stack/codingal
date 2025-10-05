import pandas as pd
import numpy as np

exdat = {"name": ["yash", "ashish", "jai"], "score":[100, 92, np.nan], "attempts":[1, 3, 4], "qualify": ['yes','no','yes']}
lables = ['a)','b)','c)']

df = pd.DataFrame(exdat, lables)
print("summary of data: ")

print(df)
