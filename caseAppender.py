import os
import shutil

def append_files_with_numeration(source_folder, target_folder, starting_number):
    # Get all the text files from the source folder
    source_files = [f for f in os.listdir(source_folder) if f.endswith('.txt')]
    
    # Sort the source files for consistency
    source_files.sort()

    # Set the current number to continue numeration
    current_number = starting_number

    # Iterate through the source files and copy them to the target folder
    for source_file in source_files:
        # Construct the full path for the source file
        source_file_path = os.path.join(source_folder, source_file)

        # Define the new filename in the target folder with the continuing numeration
        new_filename = f"acts{current_number}.txt"
        new_file_path = os.path.join(target_folder, new_filename)

        # Copy the file to the target folder
        shutil.copy(source_file_path, new_file_path)

        # Print confirmation of the copied file
        print(f"Copied: {source_file} -> {new_filename}")

        # Increment the current number for the next file
        current_number += 1

# Example usage
source_folder = '/home/aditya/Desktop/DataSet/actsAbhi'  # Replace with the path to the folder with 50 text files
target_folder = '/home/aditya/Desktop/DataSet/acts'  # Replace with the path to the 'cases' folder
starting_number = 13  # Since the last file in 'cases' is cases37.txt

append_files_with_numeration(source_folder, target_folder, starting_number)