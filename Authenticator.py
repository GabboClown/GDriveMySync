import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build, Resource

# This class uses Singleton pattern for service object creation after Authentication
class Authenticator:
    _instance = None  # Attributo statico per il Singleton

    # Method needed for Singleton pattern
    @classmethod
    def getServiceInstance(cls) -> Resource:
        if cls._instance is None:
            cls._instance = cls._auth()
        return cls._instance
    
    @classmethod
    def _auth(cls) -> Resource:
        creds = None

        # Fetches raw credentials from token.json and creates a Credentials object
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file("token.json", os.environ['SCOPES'])
        # If credentials don't exist, or if they're not valid, start auth process
        if not creds or not creds.valid:
            # Refresh credentials if needed
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            # Or create them
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', os.environ['SCOPES'])
                creds = flow.run_local_server(port=0)

            # Saves credentials for next use
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        # Creates and returns service instance
        return build('drive', 'v3', credentials=creds)
