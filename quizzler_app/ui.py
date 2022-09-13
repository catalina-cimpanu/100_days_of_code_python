from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(bg="white")
        self.canvas.config(height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, width=300,
                                                     text="question question question question question question question question ",
                                                     fill=THEME_COLOR, font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        self.score = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0, pady=(0, 20), sticky="ew")

        correct_img = PhotoImage(file="./images/true.png")
        self.correct_button = Button(image=correct_img, command=self.check_if_correct)
        self.correct_button.grid(column=0, row=2, padx=20, pady=20)

        wrong_img = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=wrong_img, command=self.check_if_false)
        self.wrong_button.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.config(bg="white")
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You reached the end of the quiz")
            self.correct_button.config(state="disable")
            self.wrong_button.config(state="disable")

    def check_if_correct(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_if_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.canvas.config(bg="green" if is_right else "red")
        self.window.after(1000, self.get_next_question)
