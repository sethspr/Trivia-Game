import json

with open("questions.json", 'r') as file:
    content = file.read()

# convert the string of 'content' to type 'list' in json format with json.loads
data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, choice in enumerate(question["choices"]):
        print(index + 1, "-", choice)

    while True:
        try:
            # convert user input to integer "correct_answer" data-type
            user_choice = int(input("Enter your answer: "))
            if 1 <= user_choice <= len(question["choices"]):
                break
            else:
                print(f"Please enter a number between 1 and {len(question['choices'])}")
        except ValueError:
            print("Please enter a valid number.")

    question["user_choice"] = user_choice

question_score = 0

# for-loop to iterate over the stored user choice to check if match with "correct_answer"
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        question_score = question_score + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = f"{index + 1}. {result} - Your answer: {question['user_choice']}, " \
              f"Correct answer: {question['correct_answer']}"
    print(message)

total_questions = len(data)

print(f"You got {question_score} out of {total_questions} correct")
print(f"Your total score is {question_score * 10} / {total_questions * 10}")

