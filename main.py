from question import Question
# Array of questions
question_prompts = [
    "The capital of Nigeria is?\n(a) Lagos\n(b) Rivers\n(c) Abuja\n\n",
    "Nigeria belong to which continent?\n(a) Africa\n(b) America \n(c) Europe\n\n",
    "China is a country in which continent?\n(a) Europe\n(b) Asia \n(c) Africa\n\n",
    "The world best footballer in 2021 is?\n(a) C.Ronaldo\n(b) L.Messi\n(c) R.lewandoski\n\n",
    "The spanish league is played in which country?\n(a) United States\n(b) England\n(c) Spain\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "c")
]
# Register a student name
student_name = input("Enter your name here: ")


# function to loop through the array of questions and generate scores
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"Hello {student_name} you answered {str(score)} / {str(len(questions))} questions correctly")


run_test(questions)
