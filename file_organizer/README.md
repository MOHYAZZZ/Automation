# Automatic File Organizer

This Python script automatically organizes your files in the Downloads folder into respective folders depending on their file types.

## Prerequisites

Make sure you have installed the following Python package:

- `tqdm`: This is used to display a progress bar in the terminal.

You can install this package using pip:

    pip install tqdm

## How to Run

To run the script, navigate to the directory containing the script and type the following command in your terminal:

    python file_organizer.py

## Functionality

The script works by moving files from the Downloads directory into categorized directories as follows:

- Images: '.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp', '.ico'
- Documents: '.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'
- Audio: '.mp3', '.wav', '.flac', '.m4a', '.aac'
- Videos: '.mp4', '.mkv', '.flv', '.mpeg', '.avi'
- Compressed: '.zip', '.rar', '.tar', '.gz'

If a directory for a particular category does not exist, the script will create it. The script also includes a progress bar in the terminal for each file type, showing the progress of the file moving operation.


## Warning

Be careful when moving files automatically, as it can overwrite existing files and might be difficult to undo. Always backup your data before running such scripts.
