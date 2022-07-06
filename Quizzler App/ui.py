from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        #Creating Window Settings
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        #Creating Main Canvas
        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(150,125,text="Quiz Question",font=("Arial",20,"italic"),fill=THEME_COLOR,width=280)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=20)
        #Creating Score Label
        self.score = Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.score.grid(column=1,row=0)
        #Creating Buttons
        correct_image = PhotoImage(file="./images/true.png")
        incorrect_image = PhotoImage(file="./images/false.png")
        self.correctButton = Button(image=correct_image,highlightthickness=0,command=self.true_pressed)
        self.correctButton.grid(column=0,row=2)
        self.incorrectButton = Button(image=incorrect_image,highlightthickness=0,command=self.false_presesed)
        self.incorrectButton.grid(column=1,row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.score = Label(text=f"Score = {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(text="You've reached the end of the quiz")
            self.correctButton.config(state="disabled")
            self.incorrectButton.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        # self.get_next_question()

    def false_presesed(self):
        # is_right = self.quiz.check_answer("False")
        self.give_feedback(self.quiz.check_answer("False"))
        # self.get_next_question()

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(background="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(background="red")
            # self.window.after(900, self.canvas.config(background="white"))
            self.window.after(1000,self.get_next_question)

