import os

def Arrage_file(all_file):
  for item in all_file:
    # Check if the current item is a file (skip folders)
    if os.path.isfile(item):

      # Skip the main Python script itself
      if item == 'Main.py':
        continue

      # Extract the file extension (e.g., "txt", "py", "jpg")
      ext = item.split(".")[1]

      # If a folder for this extension doesn't exist, create one
      # 'not' reverses the condition: it becomes True only if the folder does not exist
      if not os.path.exists(ext):
        os.makedirs(ext)

      # Create the destination path: e.g., "txt/example.txt"
      destination = os.path.join(ext, item)

      # Move (rename) the file into the corresponding extension folder
      os.rename(item, destination)


def Dearrage_file(all_file):
  script_file = 'Main'  # Base name of your main Python file (without extension)
  
  # Extract the main directory path by removing the script name from the current path
  curr = os.getcwd().split(script_file)[0]

  for folders in all_file:
    # Check if the current item is a folder
    if os.path.isdir(folders):

      # List all files inside this folder
      inside_folder_files = os.listdir(folders)

      # Move each file back to the original directory
      for inside_file in inside_folder_files:
        org_add = os.path.join(curr, folders, inside_file)  # Original full path of the file
        join = os.path.join(curr, inside_file)              # New destination path in main directory
        os.rename(org_add, join)                            # Move (rename) the file

      # Remove the now-empty folder
      os.rmdir(folders)


# Get a list of all files and folders in the current directory
all_file = os.listdir()

# Uncomment one of the following as needed:
Arrage_file(all_file)   # To organize files by extension
# Dearrage_file(all_file)   # To restore files back to the main directory
