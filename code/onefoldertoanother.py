import os
import shutil

# Define the source folder (where the .md files are currently located)
source_folder = r'C:\Users\iamab\LegalDataSet\cases'  # Replace with your source folder path

# Define the destination folder (where the .md files should be moved)
destination_folder = r'C:\Users\iamab\LegalDataSet\md_files'  # Replace with your destination folder path

# Check if the destination folder exists, if not, create it
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# List all files in the source folder
files_in_directory = os.listdir(source_folder)

# Loop through all files and move .md files to the new folder
for file_name in files_in_directory:
    if file_name.endswith('.md'):
        # Construct full file paths
        source_file = os.path.join(source_folder, file_name)
        destination_file = os.path.join(destination_folder, file_name)
        
        # Move the file
        shutil.move(source_file, destination_file)
        print(f"Moved: {file_name} to {destination_folder}")

print("All .md files have been moved.")
