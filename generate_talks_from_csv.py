import pandas as pd

df = pd.read_csv("/Users/ccarissimo/ethz-coss.github.io/February 2025 Participants - All participants (1).csv")
confirmed_speakers = df.loc[df["Will attend?"]=="Yes"]

# print(confirmed_speakers)

import glob

existing_files = glob.glob("_speakers/*.md")
print(existing_files)

for i, row in confirmed_speakers.iterrows():

    string = f"--- " \
             f"\nname: {row['What is the tentative title of your talk?']} " \
             f"\nspeakers: " \
             f"\n    - {row['Firstname']} {row['Surname']}" \
             f"\n---"
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
    path = f"_talks/{row['Firstname']}_{row['Surname']}.md"

    if path not in existing_files:
        f = open(path, "a")
        f.write(string)
        f.close()

print("There are", len(confirmed_speakers), "confirmed speakers")
