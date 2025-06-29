from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

data = []

data = [Question(item["question"], item["answer"]) for item in question_data]
quiz_brain = QuizBrain(data)

while quiz_brain.next_question():
    print(f"Your score is {quiz_brain.score}")
print(f"Game Over")
print(f"Your final score is {quiz_brain.score}")


