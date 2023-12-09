from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def get_service(creds):
    
    try:
        service = build("drive", "v3", credentials=creds)
    
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f"An error occurred: {error}")
        return
    
    return service