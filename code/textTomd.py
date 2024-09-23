import os

# Define the folder path
folder_path = r'C:\Users\iamab\LegalDataSet\cases'  # Replace with your folder path

# List all files in the directory
files_in_directory = os.listdir(folder_path)

# Loop through all files in the directory
for file_name in files_in_directory:
    # Process only .txt files
    if file_name.endswith('.txt'):
        # Create corresponding .md file name
        base_name = os.path.splitext(file_name)[0]
        output_file = base_name + '.md'

        # Read content from the .txt file with UTF-8 encoding
        try:
            with open(os.path.join(folder_path, file_name), 'r', encoding='utf-8') as txt_file:
                content = txt_file.read()
        except UnicodeDecodeError:
            print(f"Unicode error encountered while reading {file_name}. Trying with 'latin-1' encoding.")
            # Retry with a more lenient encoding (Latin-1)
            with open(os.path.join(folder_path, file_name), 'r', encoding='latin-1') as txt_file:
                content = txt_file.read()

        # Write content to the new .md file
        with open(os.path.join(folder_path, output_file), 'w', encoding='utf-8') as md_file:
            md_file.write(content)

print("All .txt files have been converted to .md files.")
