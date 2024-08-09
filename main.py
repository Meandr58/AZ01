import pandas as pd

#ПЕРВОЕ ЗАДАНИЕ

df = pd.read_csv('1990sClassicHits.csv')

#Вывод первых 5 строк данных
print(df.head())

#Вывод информации о данных
print(df.info())

#Вывод статистического описания
print(df.describe())

#ВТОРОЕ ЗАДАНИЕ

df_dz = pd.read_csv('dz.csv')

#Средняя зарплата (Salary) по городу (City)
group = df_dz.groupby('City')['Salary'].mean()
print(group)