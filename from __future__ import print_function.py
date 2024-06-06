from __future__ import print_function
import os.path
import pickle
import sys
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    user_email_to_remove = "email_to_remove@example.com"
    page_token = None

    while True:
        results = service.files().list(
            q=f"'{user_email_to_remove}' in readers or '{user_email_to_remove}' in writers",
            spaces='drive',
            fields='nextPageToken, files(id, name)',
            pageToken=page_token
        ).execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
            break

        for item in items:
            file_id = item['id']
            permissions = service.permissions().list(fileId=file_id, fields="permissions(id, emailAddress)").execute()
            for permission in permissions.get('permissions', []):
                if permission['emailAddress'] == user_email_to_remove:
                    print(f"Removing {user_email_to_remove} from {item['name']}")
                    service.permissions().delete(fileId=file_id, permissionId=permission['id']).execute()

        page_token = results.get('nextPageToken', None)
        if page_token is None:
            break

if __name__ == '__main__':
    main()