import os
from google_auth_oauthlib.flow import InstalledAppFlow

client_config = {
    "installed": {
        "client_id": os.environ.get("GOOGLE_CLIENT_ID"),
        "client_secret": os.environ.get("GOOGLE_CLIENT_SECRET"),
        "redirect_uri": "urn:ietf:wg:oauth:2.0:oob",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "grant_type": "authorization_code",
    }
}
SCOPES = [
    "openid",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
]
flow = InstalledAppFlow.from_client_config(client_config, scopes=SCOPES)
redirect_url = os.environ.get("GOOGLE_REDIRECT_URL")
client_id = os.environ.get("GOOGLE_CLIENT_ID")
