import pandas as pd

df = pd.read_csv("[Fillout] Workshop_ Smarter Societies_ Back to the Future results.csv")

# confirmed_speakers = df.loc[df["Will attend?"]=="Yes"]

# print(confirmed_speakers)

import glob

existing_files = glob.glob("_speakers/*.md")
print(existing_files)

for i, row in df.iterrows():
    string = f"--- \nname: {row['First Name']} {row['Last Name']} \nfirst_name: {row['First Name']}\nlast_name: {row['Last Name']} \n---"
    """
    Here we can add many more details that we scrape from the CSV
    like picture
    tentative title
    webpage urls
    University Affiliations
    etc
    Just need to figure out how they will be displayed
    I think it is in _layouts speaker.html
    """
    path = f"_speakers/{row['First Name']}_{row['Last Name']}.md"

    if path not in existing_files:
        f = open(path, "a")
        f.write(string)
        f.close()
