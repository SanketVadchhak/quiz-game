print("Welcome to my computer quiz!")

playing = input("Do you want to Play? ")
positive_responses = ["yes", "y", "yeah", "yep"]

if playing.lower() not in positive_responses:
    print("Exiting the game.")
    quit()
else:
    print("Let's play!")

questions = [
    {
        "question": "What does CPU stand for?",
        "answer": "central processing unit"
    },
    {
        "question": "What does GPU stand for?",
        "answer": "graphics processing unit"
    },
    {
        "question": "What does RAM stand for?",
        "answer": "random access memory"
    },
    {
        "question": "What does PSU stand for?",
        "answer": "power supply unit"
    },
    {
        "question": "What is the capital of Japan?",
        "answer": "tokyo"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "answer": "jupiter"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "answer": "william shakespeare"
    },
    {
        "question": "What is the chemical symbol for water?",
        "answer": "h2o"
    },
    {
        "question": "In which year did the Titanic sink?",
        "answer": "1912"
    },
    {
        "question": "How many continents are there?",
        "answer": "7"
    },
    {
        "question": "Which is the longest river in the world?", 
        "answer": "nile"},
    {
        "question": "What is the hardest natural substance on Earth?", 
        "answer": "diamond"},
    {
        "question": "In what country would you find the Eiffel Tower?", 
        "answer": "france"},
    {
        "question": "Who painted the Mona Lisa?", 
        "answer": "leonardo da vinci"},
    {
        "question": "What is the smallest prime number?", 
        "answer": "2"}
]

score = 0
print("Starting the quiz! 🚀")
print("-" * 20)

for q in questions:
    answer = input(q["question"] + " ")
    
    if answer.lower() == q["answer"]:
        print("Correct! ✅")
        score += 1 
    else:
        print(f"Incorrect! The answer is {q['answer']}. ❌")
    print("-" * 20)

total_questions = len(questions)
percentage = (score / total_questions) * 100

print("Quiz complete! 🎉")
print(f"You scored {score}/{total_questions}, which is {percentage:.2f}%.")