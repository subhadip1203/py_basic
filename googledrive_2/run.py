
from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=3000,open_browser=False)
           
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)

    # # Call the Drive v3 API
    # results = service.files().list(
    #     pageSize=10, fields="nextPageToken, files(id, name)").execute()
    # items = results.get('files', [])

    # if not items:
    #     print('No files found.')
    # else:
    #     print('Files:')
    #     for item in items:
    #         print(u'{0} ({1})'.format(item['name'], item['id']))

    # file_metadata = {'name': 'photo.png'}
    # media = MediaFileUpload('files/photo.png', mimetype='image/png')
    
    # file = service.files().create(body=file_metadata,
    #                                     media_body=media,
    #                                     fields='id').execute()
    # print ('File ID: %s' % file.get('id'))

   
    # save folder id in this variable
    folderId = None

    # If folder found , we make it True
    folderFound = False

    # for google drive iteration
    page_token = None
    
    response = service.files().list(
        q="mimeType='application/vnd.google-apps.folder'",
        spaces='drive',
        fields='nextPageToken, files(id, name)',
        pageToken=page_token
    ).execute()
    for file in response.get('files', []):
        
        FolderName =file.get('name',None)
        print(FolderName)
        # Process change
        if file.get('name',None) == "Habtalks" :
            folderId = file.get('id')
            folderFound = True
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break
    
    ### ------ create a folder ---------##
    if folderFound == False :
        print("creating New Folder")
        file_metadata = {
            'name': 'Habtalks',
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = service.files().create(body=file_metadata, fields='id').execute()
        folderId = file.get('id')
    
    print(folderId)

    if folderId != None:
        file_metadata = {
            'name': 'gre_fake_photo1.png',
            'parents': [folderId]
        }
        media = MediaFileUpload('files/gre_fake_photo1.png', mimetype='image/png')
        
        file = service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
        print ('File ID: %s' % file.get('id'))

if __name__ == '__main__':
    main()