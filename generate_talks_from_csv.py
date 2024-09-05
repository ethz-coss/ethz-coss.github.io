import pandas as pd

df = pd.read_csv("/Users/ccarissimo/ethz-coss.github.io/ScheduleSandbox_forWebsite_050924_v2.csv")

import glob

existing_files = glob.glob("_talks/*.md")
print(existing_files)

for i, row in df.iterrows():

    talk_title = str(row['Tentative Title']).replace(":", "-")
    if talk_title == "tbd":
        talk_title = f"tbd - {row['First Name']} {row['Last Name']}"

    string = f"--- " \
             f"\nname: {talk_title} " \
             f"\nspeakers: " \
             f"\n  - {row['First Name']} {row['Last Name']}" \
             f"\ncategories:" \
             f"\n  - Presentation" \
             f"\n---" \
             f"\n\n{talk_title}"
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
    path = f"_talks/{row['First Name']}_{row['Last Name']}.md"

    if path not in existing_files:
        f = open(path, "a")
        f.write(string)
        f.close()

# print("There are", len(confirmed_speakers), "confirmed speakers")
# print("There are", len(specified_talks), "specified talks")
