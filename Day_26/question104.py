#WAP to create quiz application.
#Step 1: Define the questions,options, and correct answers
questions = [
    {
        "question": "What is the capital of France ?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet ?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "What is 5 + 7 ?",
        "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
        "answer": "C"
    }
]

#Step 2: Initialize the score tracker
score = 0

print("---Welcome to the Simple Quiz!---\n")

#Step 3: Loop through each question
for i,q in enumerate(questions):
    print(f"Question {i+1}: {q['question']}")

    for option in q["options"]: #Print the options for the current question
        print(option)

    user_answer = input("Your answer (A,B,C, or D): ").upper().strip()

    if user_answer == q["answer"]: #Check if the answer is correct
        print("Correct !\n")
        score += 1
    else:
        print(f"Wrong. The correct answer was {q['answer']}.\n")

print("---Quiz Finished !---") #Step 4: Show final results
print(f"Your final score is: {score} out of {len(questions)}")