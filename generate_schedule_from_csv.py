import pandas as pd

df = pd.read_csv("/Users/ccarissimo/ethz-coss.github.io/February 2025 Participants - schedule_sandbox_170125_v1.csv")

days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday"}
abbr = {1: "Mo", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri"}
date = {1: "2025-02-10", 2: "2025-02-11", 3: "2025-02-12", 4: "2025-02-13", 5: "2025-02-14"}

with open("_data/program.yml", "w") as file:
    file.write("days:\n")

    previous_day = 0

    for i, row in df.iterrows():

        if previous_day != int(row["Day"]):
            day = previous_day + 1
            header = f"- name: {days[day]}\n" \
                 f"  abbr: {abbr[day]}\n" \
                 f"  date: {date[day]}\n" \
                 f"  rooms:\n" \
                 f"  - name: LEE E 101\n" \
                 f"    talks:\n"
            file.write(header)
            previous_day = day

        talk_title = str(row["Tentative Title"])
        if talk_title != "nan" or talk_title != "" or talk_title != " ":  # check if not NaN
            start_time = row["Time"].split("-")[0]
            end_time = row["Time"].split("-")[-1]
            speaker = f"{row['First Name']} {row['Last Name']}"
            if len(start_time.split(":")[0]) == 1:
                start_time = f"0{start_time}"
            if len(end_time.split(":")[0]) == 1:
                end_time = f"0{end_time}"
            print(end_time)

            virtual_tag = ""
            if str(row['virtual']) == "True":
                virtual_tag = " (v)"

            talk_title = talk_title.replace(":", " -")

            if talk_title == "tbd":
                talk_title = f"tbd - {row['First Name']} {row['Last Name']}"

            talk_title = talk_title + virtual_tag
            print(talk_title)

            talk_body = f"      - name: {talk_title}\n" \
                        f"        time_start: '{start_time}'\n" \
                        f"        time_end: '{end_time}'\n" \
                        f"        speaker: '{speaker}'\n"

            file.write(talk_body)
