import googleCalendar

def formater(events):
    reformatted_events = []

    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        summary = event["summary"]
        event_string = f"{start} - {summary}"
        if event_string[5:7] == "01":
            month = "January"
        elif event_string[5:7] == "02":
            month = "February"
        elif event_string[5:7] == "03":
            month = "March"
        elif event_string[5:7] == "04":
            month = "April"
        elif event_string[5:7] == "05":
            month = "May"
        elif event_string[5:7] == "06":
            month = "June"
        elif event_string[5:7] == "07":
            month = "July"
        elif event_string[5:7] == "08":
            month = "August"
        elif event_string[5:7] == "09":
            month = "September"
        elif event_string[5:7] == "10":
            month = "October"
        elif event_string[5:7] == "11":
            month = "November"
        else:
            month = "December"

        if int(event_string[11:13]) > 12:
            if int(event_string[14:16]) == 0:
                temp_time = int(event_string[11:13]) - 12
                time = f"{temp_time}:00 p.m."
            else:
                temp_time = int(event_string[11:13]) - 12
                time = f"{temp_time}:{int(event_string[14:16])} p.m."
        elif int(event_string[11:13]) == 12:
            if int(event_string[14:16]) == 0:
                time = f"12:00 p.m."
            else:
                time = f"12:{int(event_string[14:16])} p.m."
        elif int(event_string[11:13]) == 0 or int(event_string[11:13]) == 24:
            if int(event_string[14:16]) == 0:
                time = f"12:00 a.m."
            else:
                time = f"12:{int(event_string[14:16])} a.m."
        else:
            if int(event_string[14:16]) == 0:
                time = f"{int(event_string[11:13])}:00 a.m."
            else:
                time = f"{int(event_string[11:13])}:{int(event_string[14:16])} a.m."

        print("Formatted Time:", time)

        formatted_date = f"{month} {event_string[8]}{event_string[9]}, {event_string[0]}{event_string[1]}{event_string[2]}{event_string[3]} at {time}"
        reformatted_events.append(formatted_date)
        print(f"{event_string[11]}   {event_string[13]}")

    return reformatted_events
