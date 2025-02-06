from generate_speaker_profile_from_csv import update_speakers
from generate_talks_from_csv import update_talks
from generate_schedule_from_csv import update_schedule
import pandas as pd


if __name__ == "__main__":
    df = pd.read_csv("/Users/ccarissimo/ethz-coss.github.io/February 2025 Participants - schedule_060225.csv")

    update_speakers(df)
    update_talks(df)
    update_schedule(df)
