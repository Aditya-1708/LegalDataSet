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