from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload


def __list_files_example__(service) -> HttpError:
  try:
    # Call the Drive v3 API
    results = (
        service.files()
        .list(pageSize=10, fields="nextPageToken, files(id, name)")
        .execute()
    )
    items = results.get("files", [])

    if not items:
      print("No files found.")
      return
    
    print("Files:")
    for item in items:
      print(f"{item['name']} ({item['id']})")
    
  
  except HttpError as error:
    # TODO(developer) - Handle errors from drive API.
    print(f"An error occurred: {error}")
    return error
  
def __create_folder__(service, folder_name) -> str:

    folder_metadata = {
        "name": folder_name,
        "mimeType": "application/vnd.google-apps.folder"
    }
    
    # create the folder
    file = service.files().create(body=folder_metadata, fields="id").execute()
    
    # get the folder id
    folder_id = file.get("id")
    return folder_id


def upload_file(service, local_file_path, local_file_name, local_file_timestamp, folder_id):
    
    file_metadata = {
        "name": local_file_timestamp,
        "parents": [folder_id]
    }

    # upload
    media = MediaFileUpload(f"{local_file_path}{local_file_name}", resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print("File created, id:", file.get("id"))
  
    return

