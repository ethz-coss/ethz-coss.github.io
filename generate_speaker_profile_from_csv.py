import pandas as pd

df = pd.read_csv("February 2025 Participants - All participants.csv")

confirmed_speakers = df.loc[df["Will attend?"]=="Yes"]

print(confirmed_speakers)

import glob

existing_files = glob.glob("_speakers/*.md")
print(existing_files)

for i, row in confirmed_speakers.iterrows():
    string = f"--- \nname: {row['First name']} {row['Surname']} \nfirst_name: {row['First name']}\nlast_name: {row['Surname']} \n---"

    path = f"_speakers/{row['First name']}_{row['Surname']}.md"

    if path not in existing_files:
        f = open(path, "a")
        f.write(string)
        f.close()
