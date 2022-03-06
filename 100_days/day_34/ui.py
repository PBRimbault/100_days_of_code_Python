from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CELL_PADDING = 15

test_text = "This is a whole lot of text that should probably actually be a lorem ipsum but I'm too lazy to go find it."

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg='white')        
        self.question_text = self.canvas.create_text(
            150, 125, 
            text=test_text, 
            width=250, 
            fill="black", 
            font=('Arial', 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=CELL_PADDING, padx=CELL_PADDING)

        #Labels
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0, pady=CELL_PADDING, padx=CELL_PADDING)

        #Buttons
        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")

        self.true_button = Button(
            image=true_img,  
            highlightthickness=0, 
            relief=FLAT, 
            borderwidth=0, 
            command=self.answer_true
        )
        self.true_button.grid(column=0, row=2, pady=CELL_PADDING, padx=CELL_PADDING)

        self.false_button = Button(
            image=false_img,  
            highlightthickness=0, 
            relief=FLAT, 
            borderwidth=0, 
            command=self.answer_false
        )
        self.false_button.grid(column=1, row=2, pady=CELL_PADDING, padx=CELL_PADDING)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
