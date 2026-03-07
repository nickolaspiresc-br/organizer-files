'''
tratamento de erros;
poder criar mais subpastas, o quanto o usuario quiser;
'''

#Import modules
from pathlib import Path
import shutil

#Create a folder with name choose for user in folder "Downloads"
folder_user = input("\nWhat name of your folder?: ")
folder_main = Path() / "Downloads" / folder_user
folder_main.mkdir(parents=True, exist_ok=True)

#Folders of each type file extension in folder created for user
def create_folders(type_folder,main_path):
    sub_folder = Path.home() / main_path / type_folder
    sub_folder.mkdir(parents=True, exist_ok=True)

subfolders_main = ["Documents","Compressed","Spreadsheets","Images",
                   "Executables","Audios","Videos","Presentations"]

for name in subfolders_main:
    create_folders(name,folder_main)

print("\nFolder created.\n")

#Create files
file_user = input("What is your file name and extension? ").lower()
file_user = folder_main / file_user
file_user.touch()

print("\nFile created")

#Analyze the created file and move to folder of file extension
extensions = {".pdf":"Documents",
              ".txt":"Documents",
              ".png":"Images",
              ".jpg":"Images",
              ".zip":"Compressed"
              }

for extension, folder in extensions.items():
    if file_user.suffix==extension:
        path_complete = Path.home() / folder_main / folder
        shutil.move(file_user,path_complete)