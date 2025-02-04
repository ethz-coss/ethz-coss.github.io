import pandas as pd
import os

df = pd.read_csv("/Users/ccarissimo/ethz-coss.github.io/February 2025 Participants - schedule_040225.csv")
print(df)
import glob

existing_files = glob.glob("_talks/*.md")
print(existing_files)

"""
expects a CSV file with the following columns:
First Name, Last Name, Tentative Title, virtual
"""

for i, row in df.iterrows():
    if len(str(row['Last Name'])) > 1:  # exclude empty string last names
        talk_title = str(row["Tentative Title"])
        if talk_title != "nan" and talk_title != "" and talk_title != " " and talk_title != "none":  # check if not NaN
            virtual_tag = ""
            # print(row["virtual"])
            if str(row['virtual']) == "Virtual":
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
                print(path)
            else:
                os.remove(path)
                f = open(path, "a")
                f.write(string)
                f.close()
                print(path)

# print("There are", len(confirmed_speakers), "confirmed speakers")
# print("There are", len(specified_talks), "specified talks")
existing_speaker_files = set([x.strip("_speakers/") for x in glob.glob("_speakers/*.md")])
existing_talk_files = set([x.strip("_talks/") for x in glob.glob("_talks/*.md")])
print("speakers minus talks")
print(existing_speaker_files.symmetric_difference(existing_talk_files))
