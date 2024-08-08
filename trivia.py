import json

with open("questions.json", 'r') as file:
    content = file.read()

# convert the string of 'content' to type 'list' in json format with json.loads
data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, choice in enumerate(question["choices"]):
        print(index + 1, "-", choice)

    user_choice = int(input("Enter your answer: "))