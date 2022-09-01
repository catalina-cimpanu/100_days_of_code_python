from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    new_question = Question(item["question"], item["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.game_ended()
