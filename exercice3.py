import pandas as pd

df = pd.read_csv('notes.csv')

max = 0
min = 20
compteur = 0
for index, row in df.iterrows():
    if (row["Note"] > max):
        max = row["Note"]
    if (row["Note"] < min):
        min = row["Note"]
    if (row["Note"] >= 10):
        compteur += 1
 
print(f"La note la plus haute est {max}.")
print(f"La note la plus basse est {min}.")
print(f"Le nombre d'étudiants ayant une note au dessus de la moyenne est de {compteur}.")
