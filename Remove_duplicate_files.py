import os
import hashlib
folder_path = "C:\Users\DELL\OneDrive\Desktop\DSA Python 2\demo" # use \\ for manually type folder address

sets = set()

def hash_file(file_name):
  hash_ = hashlib.md5()
  file_join = os.path.join(f'{folder_path}',file_name) 

  file = open(file_join,'rb')
  while (chunk := file.read(4034)):
    hash_.update(chunk)

  file.close()
  return hash_.hexdigest()


try:
  all_files = os.listdir(folder_path) # Reading All Files In the Folder

  for files in all_files:
    hash_value = hash_file(files)

    if (hash_value in sets):
      permission_user = input(f"Deleting {files} --> Yes/No")

      if (permission_user == 'Yes'):
        current_file = os.path.join(f'{folder_path}',files)
        os.remove(current_file)
        print(f"{files} is Deleted")
      else:
        print(f"{files} Not Deleted")

    else:
      sets.add(hash_value)

except Exception as error:
  print(f"error : {error}") # Any Error Occured


