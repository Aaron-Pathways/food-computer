
from factories import credential_factory, service_factory
import actions, sys, configparser
from datetime import datetime

def main():
  try:
    
    config = configparser.ConfigParser()
    
    config.read(["/home/aaron.pathways/projects/food-computer/config.ini"])
    group = config['group']['your_group']
    
    folder_id = config['group_map'][group]
    
    local_file_path = sys.argv[1]
    local_file_name = sys.argv[2]
    local_file_timestamp = sys.argv[3]

    
    creds = credential_factory.get_creds(local_file_path)
    service = service_factory.get_service(creds)
    actions.upload_file(service, local_file_path, local_file_name, local_file_timestamp, folder_id)
  except Exception as e:
    print(e.args)
    return e



main()
