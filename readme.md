# Code:

## 1. Getting Credentials

### Main Resources:
    
- `def get_creds() -> Credentials` --- credential_factory.py

- `Scopes`:
    - https://www.googleapis.com/auth/drive.metadata.readonly
    - https://www.googleapis.com/auth/drive.file


Using the scopes located in the `SCOPES` list, it first attempts to find local valid credentials. If none are found, valid credendials are generated using the client's secret.

## 2. Getting Service

### Main Resources:

- `def get_service(creds)` --- service_factory.py

Using the credentials, a service is build that will be responsible for any CRUD action with Drive api.

## 3. Uploading File

### Main Resources:
- `def upload_file(service, local_file_path, local_file_name, local_file_timestamp, folder_id)` --- actions.py

After the service has been successfully generated, the `upload_file(service, et al)` function can commence. It recieves several arguments that are being passed in via a mix of `sys.argv`'s, config file params, and a `service` object



# links:

https://raspberrypi-guide.github.io/electronics/using-usb-webcams
https://developers.google.com/workspace/guides/create-credentials#web-application
https://developers.google.com/drive/api/guides/manage-uploads#python
https://developers.google.com/drive/api/quickstart/python
https://thepythoncode.com/article/using-google-drive--api-in-python
https://www.airplane.dev/blog/cron-versus-anacron
