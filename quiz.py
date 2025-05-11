import pyfiglet

ascii_art = pyfiglet.figlet_format("Quiz Game")
print(ascii_art)

# Quiz questions and answers
questions = [
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Jupiter", "C. Saturn", "D. Neptune"],
        "answer": "B"
    },
    {
        "question": "Who is known as the father of computers?",
        "options": ["A. Charles Babbage", "B. Alan Turing", "C. John von Neumann", "D. Ada Lovelace"],
        "answer": "A"
    },
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A. Oxygen", "B. Gold", "C. Osmium", "D. Silver"],
        "answer": "A"
    },
    {
        "question": "What is the speed of light in vacuum?",
        "options": ["A. 300,000 km/s", "B. 150,000 km/s", "C. 1,000 km/s", "D. 500,000 km/s"],
        "answer": "A"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. William Shakespeare", "B. Charles Dickens", "C. Mark Twain", "D. Jane Austen"],
        "answer": "A"
    },
    {
        "question": "Which programming language is known as the backbone of web development?",
        "options": ["A. Python", "B. JavaScript", "C. Java", "D. C++"],
        "answer": "B"
    },
    {
        "question": "What is the smallest unit of life?",
        "options": ["A. Atom", "B. Molecule", "C. Cell", "D. Organ"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Mercury", "D. Pluto"],
        "answer": "B"
    },
    {
        "question": "What is the chemical formula for water?",
        "options": ["A. CO2", "B. H2O", "C. O2", "D. CH4"],
        "answer": "B"
    }
]

score = 0

for i, q in enumerate(questions, start=1):
    print(f"Question {i}: {q['question']}")
    for option in q["options"]:
        print(option)
    user_answer = input("Your answer (A, B, C, D): ").strip().upper()

    while user_answer not in ["A", "B", "C", "D"]:
        user_answer = input("Invalid input. Please enter A, B, C, or D: ").strip().upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! The correct answer was {q['answer']}.")
    print(f"Current score: {score}\n")

print("Quiz Over!")
print(f"Your final score is {score}/10.")

if score >= 9:
    print("Excellent work!")
elif score >= 6:
    print("Good effort!")
elif score >= 3:
    print("Not bad, keep learning.")
else:
    print("Better luck next time.")