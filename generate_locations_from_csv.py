import pandas as pd

df = pd.read_csv("/Users/ccarissimo/ethz-coss.github.io/February 2025 Participants - locations.csv")

with open("_data/location.yml", "w") as file:
    file.write("places:\n")

    for i, row in df.iterrows():
        lat = float(str.replace(row['lat'], ",", "."))
        lng = float(str.replace(row['lng'], ",", "."))

        talk_body = f"      - name: {row['name']}\n" \
                    f"        lat: {lat}\n" \
                    f"        lng: {lng}\n" \
                    f"        type: {row['type']}\n" \
                    f"        website: '{row['website']}'\n"

        file.write(talk_body)
