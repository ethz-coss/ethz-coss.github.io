import pandas as pd
import glob
import os


def update_speakers(df):
    existing_files = glob.glob("_speakers/*.md")
    print(existing_files)

    for speaker_path in existing_files:
        os.remove(speaker_path)

    for i, row in df.iterrows():
        talk_title = str(row["Tentative Title"])
        if talk_title != "nan" and talk_title != "" and talk_title != " " and talk_title != "none":  # check if not NaN
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

            f = open(path, "a")
            f.write(string)
            f.close()

    existing_files = glob.glob("_speakers/*.md")
    print("There are", len(existing_files), "confirmed speakers")


if __name__ == "__main__":
    df = pd.read_csv("/Users/ccarissimo/ethz-coss.github.io/February 2025 Participants - schedule_060225.csv")
    update_speakers(df)
