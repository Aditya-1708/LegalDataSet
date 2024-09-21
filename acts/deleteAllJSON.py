import os

def delete_json_files_in_folder(folder_path):
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file ends with .json
        if filename.endswith('.json'):
            # Construct full file path
            file_path = os.path.join(folder_path, filename)
            try:
                # Remove the file
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")

# Example usage
folder_path = '/home/aditya/Desktop/DataSet/acts'  # Replace with the actual path to your folder
delete_json_files_in_folder(folder_path)