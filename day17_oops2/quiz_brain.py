class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.score += 1
        self.question_number += 1
        answer = input(f"Question  {self.question_number}: {current_question.question} Write the answer: ")
        if answer == current_question.answer:
            self.score += 1
            self.question_number += 1
            return True
        else:
            return False