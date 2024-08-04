import pandas as pd

df = pd.read_csv('notes.csv')

total = 0
for index, row in df.iterrows():
    total += row["Note"]

moyenne = total / len(df.index)
print(f"La moyenne des étudiants est de {round(moyenne, 2)}")