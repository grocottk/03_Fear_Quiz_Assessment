
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
        self.question_number.set(0)

        # Initialising Start Frame (from "01_Mystery_Box_Outline.py")
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Start Heading (Row 0)
        self.quiz_heading_label = Label(self.start_frame, text="Fear Quiz", font="Arial 25 bold", justify=CENTER, padx=10, pady=10)
        self.quiz_heading_label.grid(row=0)

        # Start Instructions (Row 1)
        self.start_instructions = Label(self.start_frame, text="Please enter the number of questions that you would like to answer in the box below.", 
                                        font="Arial 10 italic", justify=LEFT, padx=10, pady=10, wrap=350)
        self.start_instructions.grid(row=1)

        # Number Entry Box (Row 2) [from "01_Mystery_Box_Outline.py"]
        self.number_entry_box = Entry(self.start_frame, width=50)
        self.number_entry_box.grid(row=2)

        # Start Error Message Area (Row 3)
        self.start_error_message_area = Label(self.start_frame, font="Arial 10")
        self.start_error_message_area.grid(row=3)

        # Start Buttons Frame (Row 4) [inspired by "08b_Game_Export_GUI_Version_2.py" and "05_Game_Playable.py"]
        self.start_buttons_frame = Frame(pady=15)
        self.start_buttons_frame.grid(row=4)

        # Help Button (Row 0, Column 0)
        self.help_button = Button(self.start_buttons_frame, text="Help", font="Arial 10", pady=5, padx=10, bg="orange")
        self.help_button.grid(row=0, column=0, padx=10)

        # Check Button (Row 0, Column 1)
        self.check_button = Button(self.start_buttons_frame, text="Check Answer", font="Arial 10", pady=5, padx=10, bg="yellow",
                                command=self.check_question_amount)
        self.check_button.grid(row=0, column=1, padx=10)

        # Start Button (Row 0, Column 2)
        self.start_button = Button(self.start_buttons_frame, text="Start", font="Arial 10", pady=5, padx=10, bg="green", fg="lime",
                                command=lambda: self.to_quiz)
        self.start_button.grid(row=0, column=2, padx=10)

    # Question Amount Checking (inspired by "02_Start_GUI.py", specifically the segement titled "check_funds",
    # ... and "12g_Assembled_Program.py")
    def check_question_amount(self):
        
        # Get initial data
        question_amount = self.number_entry_box.get()

        # Sets initial varables, including background colour and error checking
        error_background = "pink"
        success_background = "green"
        has_errors = "no"

        try:
            question_amount = int(question_amount)

            # If the question amount is less than 1, give an error message
            if question_amount < 1:
                has_errors = "yes"
                error_feedback = "Sorry, the lowest number of questions that you can be asked is 1."

            # If the question amount is more than 113, give an error message
            elif question_amount > 113:
                has_errors = "yes"
                error_feedback = "Sorry, the highest number of questions that you can be asked is 113."
            
        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a whole number between 1 and 113"

        if has_errors == "yes":
            # If errors are present, change the error area
            self.start_error_message_area.config(bg=error_background)
            self.start_error_message_area.config(text=error_feedback)

        else:
            # Set total questions to the question_amount variable
            self.start_error_message_area.config(bg=success_background)
            self.start_error_message_area.config(text="This is a valid number of questions to be asked")
            self.start_error_message_area.config(fg="lime")
            self.question_number.set(question_amount)

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
