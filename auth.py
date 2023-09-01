import os.path
import serverAuth
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    'https://www.googleapis.com/auth/calendar'
]

def get_authorization_url():
    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
    authorization_url, _ = flow.authorization_url(prompt='consent')

    print(f"Authorization URL: {authorization_url}")  # Print the authorization URL
    return authorization_url
