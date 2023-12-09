
from factories import credential_factory, service_factory
import actions, sys, configparser
from datetime import datetime

def main():
  config = configparser.ConfigParser()
  config.read("config.ini")
  folder_id = config['group']['your_group']

  local_file_path = sys.argv[1]
  local_file_name = sys.argv[2]
  local_file_timestamp = sys.argv[3]  

  creds = credential_factory.get_creds()
  service = service_factory.get_service(creds)
  actions.list_files_example(service)
  actions.upload_file(service, local_file_path, local_file_name, local_file_timestamp, folder_id)


if __name__ == "__main__":
  main()
