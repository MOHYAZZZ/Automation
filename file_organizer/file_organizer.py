import os
import shutil
from tqdm import tqdm

# Specify the directory you want to organize
path = os.path.expanduser("~/Downloads")

# File types and their corresponding directories
file_type_directory_mapping = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp', '.ico'],
    'Docs': ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.flac', '.m4a', '.aac'],
    'Videos': ['.mp4', '.mkv', '.flv', '.mpeg', '.avi'],
    'Compressed': ['.zip', '.rar', '.tar', '.gz'],
}

for file_type, extensions in file_type_directory_mapping.items():
    directory_path = os.path.join(path, file_type)
    if not os.path.isdir(directory_path):
        os.mkdir(directory_path)  # create a directory if it does not exist

    # Get a list of files to be moved for this type
    files_to_move = [file for file in os.listdir(path) if any(file.endswith(extension) for extension in extensions)]
    
    # Create a progress bar
    with tqdm(total=len(files_to_move), desc=f"Moving {file_type}", ncols=75) as pbar:
        for file in files_to_move:
            file_path = os.path.join(path, file)
            shutil.move(file_path, directory_path)  # move the file to its directory
            pbar.update(1)  # update the progress bar
