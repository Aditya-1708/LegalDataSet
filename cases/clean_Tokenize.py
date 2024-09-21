import os
import json
import re

def clean_text(text):
    # Remove newlines
    text = text.replace("\n", " ").replace("\r", " ")

    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)

    # Remove unnecessary punctuation (keeping periods, commas, question marks, exclamations, and hyphens)
    text = re.sub(r'[^\w\s.,?!-]', '', text)

    # Strip leading/trailing spaces
    text = text.strip()

    return text

def tokenize_string(s):
    # Split the string using periods, commas, and spaces as delimiters
    tokens = re.split(r'[ ,.]', s)
    # Remove empty tokens
    tokens = [token for token in tokens if token]
    return tokens

def process_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):  # Process only .txt files
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                original_string = file.read()
                
            # Clean the text
            cleaned_string = clean_text(original_string)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(cleaned_string)
            # Tokenize the cleaned string
            # tokens = tokenize_string(cleaned_string)

            # Create a JSON-compatible dictionary
            # data = {
            #     'tokens': tokens
            # }

            # Define the output JSON file path
            # json_filename = os.path.splitext(filename)[0] + 'txt'
            # json_file_path = os.path.join(folder_path, json_filename)
            
            # Write the tokens to a JSON file
            # with open(json_file_path, 'w', encoding='utf-8') as json_file:
            #     json.dump(data, json_file, indent=4)

# Example usage
folder_path = '/home/aditya/Desktop/DataSet/cases'  # Replace with your folder path
process_files_in_folder(folder_path)