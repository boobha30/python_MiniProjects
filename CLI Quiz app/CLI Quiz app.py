questions = [
    {
        "question": "What is the capital of Singapore?",
        "options": ["a) Singapore", "b) Kuala Lumpur", "c) Jakarta"],
        "answer": "a"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["a) Earth", "b) Jupiter", "c) Saturn"],
        "answer": "b"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["a) Au", "b) Ag", "c) Fe"],
        "answer": "a"
    }
]
score = 0
for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    answer = input("Enter your answer (a, b, or c): ")
    if answer.lower() == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
print(f"Your final score is: {score}/{len(questions)}") 