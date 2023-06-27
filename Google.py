import os
import json
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SERVICE_ACCOUNT_FILE = 'credentials.json'
SCOPES = ['https://mail.google.com/']

creds = None

if os.path.exists(SERVICE_ACCOUNT_FILE):
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )
    with open(SERVICE_ACCOUNT_FILE, 'w') as f:
        f.write(creds.to_json())

# Use the creds object to build the Gmail API service
service = build('gmail', 'v1', credentials=creds)

# Perform Gmail API operations using the 'service' object
#  list the user's Gmail labels

results = service.users().labels().list(userId='me').execute()
labels = results.get('labels', [])

if not labels:
    print('No labels found.')
else:
    print('Labels:')
    for label in labels:
        print(label['name'])
