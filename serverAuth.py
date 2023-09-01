import os.path
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    'https://www.googleapis.com/auth/calendar'
]


def get_authorization_url():
    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json",
        scopes=SCOPES,
        redirect_uri="http://localhost:60895/"  # Replace with your actual redirect URI
    )

    authorization_url, _ = flow.authorization_url(prompt='consent')

    print(f"Authorization URL: {authorization_url}")  # Print the authorization URL

    return authorization_url


# Example usage
authorization_url = get_authorization_url()
print("Please visit this URL to authorize your application:")
print(authorization_url)
