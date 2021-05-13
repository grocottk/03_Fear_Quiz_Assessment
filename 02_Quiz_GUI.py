
# Initial Start GUI from "01_Start_GUI.py"

# This file will become Component 1 of the "Fear Quiz Assessment".
# [Note: This file has now been edited on a new device, 
# ... so a new build of the code can now be marked as currently active]

# Import Statements as follows (from "01_Mystery_Box_Outline.py"):
from tkinter import *
import random
from functools import partial # This prevents unwanted windows from opening

# Start Class (with various portions taken from "01_Mystery_Box_Outline.py" and also "02_Converter_GUI.py")
class Start:
    def __init__(self, parent):

        # Defining Variables segment
        self.question_number = IntVar()
        self.question_number.set(10)

        # Initialising Start Frame (from "01_Mystery_Box_Outline.py")
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Start Heading (Row 0)
        self.quiz_heading_label = Label(self.start_frame, text="Fear Quiz", font="Arial 25 bold", justify=CENTER, padx=10, pady=10)
        self.quiz_heading_label.grid(row=0)

        # Start Buttons Frame (Row 4) [inspired by "08b_Game_Export_GUI_Version_2.py" and "05_Game_Playable.py"]
        self.start_buttons_frame = Frame(pady=15)
        self.start_buttons_frame.grid(row=1)

        # Help Button (Row 0, Column 0)
        self.help_button = Button(self.start_buttons_frame, text="Help", font="Arial 10", pady=5, padx=10, bg="orange")
        self.help_button.grid(row=0, column=0, padx=10)

        # Start Button (Row 0, Column 2)
        self.start_button = Button(self.start_buttons_frame, text="Start", font="Arial 10", pady=5, padx=10, bg="green", fg="lime",
                                command=lambda: self.to_quiz)
        self.start_button.grid(row=0, column=1, padx=10)

    # To Quiz function (inspired by "02_Start_GUI.py", specifically the "to_game" section)
    def to_quiz(self, question_amount):

        # Retrieve starting balance
        question_amount = self.number_entry_box.get()
        
        # Takes variables to the quiz class
        Quiz(self, question_amount)

        # Hide start up window
        root.withdraw()

# Quiz Class (many parts of this class have been inspired by "00_Compiled_Version_6.py")
class Quiz:
    def __init__(self, qestion_amount):

        # GUI Setup (from "00_Compiled_Version_6.py")
        self.quiz_frame = Toplevel()

        # Establishes quiz frame (inspired by "00_Compiled_Version_6.py")
        self.quiz_frame = Frame(self.quiz_box)
        self.quiz_frame.grid()

        # Question number label (Row 0)
        self.question_number_label = Label(self.game_frame, text="1/100", font="Arial 10 bold",
                                padx=10, pady=10, justify=CENTER)
        self.question_number_label.grid(row=0)

# Main Routine (edited from "02_Start_GUI.py")
if __name__ == "__main__":
    root = Tk()
    root.title("Fear Quiz")
    something = Start(root)
    root.mainloop()
