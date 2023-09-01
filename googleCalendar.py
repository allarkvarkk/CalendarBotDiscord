import datetime as dt
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import formater
import auth  # Import the auth module

def get_upcoming_events():
    authorization_url = auth.get_authorization_url()

    creds = Credentials.from_authorized_user_file("token.json")

    try:
        service = build("calendar", "v3", credentials=creds)

        now = dt.datetime.now().isoformat() + "Z"

        event_result = service.events().list(calendarId="primary", timeMin=now, maxResults=10, singleEvents=True,
                                             orderBy="startTime").execute()

        events = event_result.get("items", [])

        if not events:
            return "No upcoming events found!"

        event_strings = []
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            summary = event["summary"]
            event_string = f"{start} - {summary}"
            event_strings.append(event_string)

        return formater.formater(events)

    except HttpError as error:
        return f"An error occurred: {error}"
