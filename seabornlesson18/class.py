import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb

df = pd.read_csv(r"E:\cods\codingal\seabornlesson18\USA_Housing.csv")
df.head(10)
# print(df.info())
# print(df.describe())
# print(df.columns)
# sb.pairplot(df)
sb.heatmap(df.select_dtypes(include = 'number').corr(), annot = True)
plt.show()