from App.Exceptions.ServiceNotRegisteredException import ServiceNotRegisteredException
from googleapiclient.http import MediaIoBaseDownload
import io
import os

class DriveRepository:
    _service = None

    def __init__(self, service=None):
        if DriveRepository._service is None:
            if service is not None:
                DriveRepository._service = service
            else:
                # _service will be used as a Singleton object, but it needs a value
                raise ServiceNotRegisteredException("You need to pass Google Resource service on first initialization")
            
    def listFilesInFolder(self, folder_id, fileFields):
        results = DriveRepository._service.files().list(q=f"'{folder_id}' in parents", fields=f"files({fileFields})").execute()
        files = results.get('files', [])

        return files
    
    def fileDownload(self, file_id, local_folder):
        file_metadata = DriveRepository._service.files().get(fileId=file_id).execute()
        file_name = file_metadata['name']

        # Ensure local folder exists
        if not os.path.exists(local_folder):
            os.makedirs(local_folder)

        # Download the file
        request = DriveRepository._service.files().get_media(fileId=file_id)
        file_path = os.path.join(local_folder, file_name)
        fh = io.FileIO(file_path, 'wb')

        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
            print(f"Downloading {int(status.progress() * 100)}%.")

        print(f"File downloaded: {file_path}")
        return file_path
