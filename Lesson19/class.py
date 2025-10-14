import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb

df = pd.read_csv(r"E:\cods\codingal\Lesson19\Weather Dataset - Trial Activity DataSet.csv.csv")
# print(df.head())
# print(df.info())
# sb.barplot(x="humidity", y="temperature", data=df)
# sb.distplot(df["humidity"], kde=False, rug=True)
# sb.jointplot(x="humidity", y="temperature", data=df, kind='kde')
# sb.stripplot(x="weather_type", y="temperature", hue='weather_type',data=df)
# sb.swarmplot(x= 'humidity', y='temperature', data = df)
# sb.boxplot(x='humidity', y='temperature', hue='weather_type',data=df )
sb.pointplot(x='humidity', y='temperature', hue="weather_type", data=df)
plt.show()