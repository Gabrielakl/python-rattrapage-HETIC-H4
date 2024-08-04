import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('notes.csv')

nombre_etudiant_par_note = []

for i in range(21):
    nombre_etudiant_par_note.append(0)

for index, row in df.iterrows():
    nombre_etudiant_par_note[row["Note"]] += 1

note_df = pd.DataFrame(nombre_etudiant_par_note, columns=['Nombres'])

ax = note_df.plot.bar(column=["Nombres"], figsize=(10, 8), color='#800080', edgecolor='black')

plt.title("Nombre d'étudiants en fonction de leur note")
plt.xlabel('Note')
plt.ylabel("Nombre d'étudiants")
ax.set_yticks(range(4))
ax.set_xticks(range(21))

plt.show()
