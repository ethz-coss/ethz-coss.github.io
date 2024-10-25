import pandas as pd

df = pd.read_csv("/Users/ccarissimo/ethz-coss.github.io/ScheduleSandbox_forWebsite_251024_v3.csv")

import glob

existing_files = glob.glob("_talks/*.md")
print(existing_files)

"""
expects a CSV file with the following columns:
First Name, Last Name, Tentative Title, virtual
"""

for i, row in df.iterrows():

    virtual_tag = ""
    # print(row["virtual"])
    if str(row['virtual']) == "True":
        virtual_tag = " (v)"

    talk_title = str(row['Tentative Title']).replace(":", " -")
    if talk_title == "tbd":
        talk_title = f"tbd - {row['First Name']} {row['Last Name']}"

    talk_title = talk_title + virtual_tag

    string = f"--- " \
             f"\nname: {talk_title}" \
             f"\nspeakers: " \
             f"\n  - {row['First Name']} {row['Last Name']}" \
             f"\ncategories:" \
             f"\n  - Presentation" \
             f"\n---" \
             f"\n\n{talk_title}"

    path = f"_talks/{row['First Name']}_{row['Last Name']}.md"

    if path not in existing_files:
        f = open(path, "a")
        f.write(string)
        f.close()

# print("There are", len(confirmed_speakers), "confirmed speakers")
# print("There are", len(specified_talks), "specified talks")
