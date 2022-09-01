class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} True or False?: ").lower()
        self.check_answer(user_answer, current_question.answer)
        print(f"Your current score is {self.score}/{self.question_number}.\n")


    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print(f"Correct. \nThe correct answer was: {correct_answer}.")
            self.score += 1
        else:
            print("False.")

    def game_ended(self):
        print(f"You've completed the game.\nYour score was {self.score}/{len(self.question_list)}")
