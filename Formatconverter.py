import json
with open('DataSet.json') as f:
    data = json.load(f)

# Arrays to store questions and answers
questions = []
answers = []

# Loop through each item in data
for item in data['data']:
    questions.append(item['question'])
    answers.append(item['answer'])

# Create a new dictionary to store questions and answers
output_data = {
    "questions": questions,
    "answers": answers
}

# Write the new data to a JSON file
with open('output.json', 'w') as json_file:
    json.dump(output_data, json_file, indent=4)

print("Data has been stored in output.json")
