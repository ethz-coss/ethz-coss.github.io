import pandas as pd

df = pd.read_csv("/Users/ccarissimo/ethz-coss.github.io/February 2025 Participants - AllParticipants_050924.csv")
confirmed_speakers = df.loc[df["Will attend?"]=="Yes"]
specified_talks = confirmed_speakers.loc[confirmed_speakers["What is the tentative title of your talk?"] != "tbd"]

# print(confirmed_speakers)

import glob

existing_files = glob.glob("_talks/*.md")
print(existing_files)

for i, row in confirmed_speakers.iterrows():

    talk_title = row['What is the tentative title of your talk?'].replace(":", "-")
    if talk_title == "tbd":
        talk_title = f"tbd - {row['Firstname']} {row['Surname']}"

    string = f"--- " \
             f"\nname: {talk_title} " \
             f"\nspeakers: " \
             f"\n  - {row['Firstname']} {row['Surname']}" \
             f"\ncategories:" \
             f"\n  - Presentation" \
             f"\n---" \
             f"\n\n{row['What is the tentative title of your talk?']}"
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
print("There are", len(specified_talks), "specified talks")
