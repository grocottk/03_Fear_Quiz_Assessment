
# Initial Start GUI from "01_Start_GUI.py"

# This file will become Component 1 of the "Fear Quiz Assessment".
# [Note: This file has now been edited on a new device, 
# ... so a new build of the code can now be marked as currently active]

# Import Statements as follows (from "01_Mystery_Box_Outline.py"):
from tkinter import *
import random
from functools import partial # This prevents unwanted windows from opening

# The majority of the below code is from the program known as "05_Game_Playable.py"

# Start Class (with various portions taken from "01_Mystery_Box_Outline.py" and also "02_Converter_GUI.py")
class Start:
    def __init__(self, parent):

        # GUI to find starting balance and stakes from the user:
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Test Button (Row 0)
        self.push_me_button = Button(self.start_frame, text="Press This", command=self.to_game)
        self.push_me_button.grid(row=0, pady=5)

    def to_game(self):

        # Set question amount to 20
        question_amount = 20

        Quiz(self, question_amount)

        # Hide start up window
        self.start_frame.destroy()

class Quiz:
    def __init__(self, partner, question_amount):

        print(question_amount)

        # Initialise question variable
        self.question = IntVar()

        # Set question variable to question amount entered by user at start of game
        self.question.set(question_amount)

        # GUI Setup
        self.quiz_box = Toplevel()

        # If users press cross at top, the game quits
        self.quiz_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        # Defining Game Frame
        self.quiz_frame = Frame(self.quiz_box, padx=10, pady=10)
        self.quiz_frame.grid()

        # Question number label (Row 0)
        self.question_number_label = Label(self.quiz_frame, text="1/{}".format(question_amount), font="Arial 10 bold",
                                padx=10, pady=10, justify=CENTER)
        self.question_number_label.grid(row=0)

        # Question text [Part 1] (Row 1)
        self.question_text_part_one = Label(self.quiz_frame, text="The word...", font="Arial 15",
                                        padx=10, pady=10, justify=LEFT)
        self.question_text_part_one.grid(row=1)

        # Fear Name (Row 2)
        self.fear_name_label = Label(self.quiz_frame, text="[Fear Name]", font="Arial 25",
                                        padx=10, pady=10, justify=CENTER)
        self.fear_name_label.grid(row=2)

        # Question text [Part 2] (Row 3)
        self.question_text_part_two = Label(self.quiz_frame, text="represents a fear of...", font="Arial 15",
                                        padx=10, pady=10, justify=LEFT)
        self.question_text_part_two.grid(row=3)

    def to_quit(self):

        root.destroy()

# Main Routine (edited from "02_Start_GUI.py")
if __name__ == "__main__":
    root = Tk()
    root.title("Fear Quiz")
    something = Start(root)
    root.mainloop()
