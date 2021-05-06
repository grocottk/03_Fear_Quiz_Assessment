
# This file will become Component 1 of the "Fear Quiz Assessment".
# [Note: This file has now been edited on a new device, 
# ... so a new build of the code can now be marked as currently active]

# Import Statements as follows (from "01_Mystery_Box_Outline.py"):
from tkinter import *
import random
from functools import partial # This prevents unwanted windows from opening

# Start Class (with various portions taken from "01_Mystery_Box_Outline.py")
class Start:
    def __init__(self, parent):

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
        self.start_error_message_area = Label(self.start_frame, text="")
        self.start_error_message_area.grid(row=3)

        # Start Buttons Frame (Row 4) [inspired by "08b_Game_Export_GUI_Version_2.py" and "05_Game_Playable.py"]
        self.start_buttons_frame = Frame(pady=15)
        self.start_buttons_frame.grid(row=4)

        # Help Button (Row 0, Column 0)
        self.help_button = Button(self.start_buttons_frame, text="Help", font="Arial 10", pady=5, padx=10, bg="orange")
        self.help_button.grid(row=0, column=0, padx=50)

        # Start Button (Row 0, Column 1)
        self.start_button = Button(self.start_buttons_frame, text="Start", font="Arial 10", pady=5, padx=10, bg="green")
        self.start_button.grid(row=0, column=1, padx=50)

    # Question Amount Checking (inspired by "02_Start_GUI.py", specifically the segement titled "check_funds")
    def check_question_amount(self):
        
        # Get initial data
        question_amount = self.number_entry_box.get()

        # Sets initial varables, including background colour and error checking
        error_background="pink"
        has_errors = "no"

        # Change background colour to white for testing purposes
        self.number_entry_box.config(bg="white")
        self.number_entry_box.config(text="")

        try:
            question_amount = int(question_amount)

            if starting_balance =< 0:
                has_errors = "yes"
                error_feedback = "Sorry, the lowest number of questions that you can be asked is 1."

            elif starting_balance > 114:
                has_errors = "yes"
                error_feedback = "Sorry, the highest number of questions that you can be asked is 113."

            else:
                has_errors="no"
            
        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a whole number between 1 and 113"

        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_background)
            self.amount_error_label.config(text=error_feedback)

        else:
            # Set starting balance to amount entered by user
            self.starting_funds.set(starting_balance)

# Main Routine (edited from "02_Start_GUI.py")
if __name__ == "__main__":
    root = Tk()
    root.title("Fear Quiz")
    something = Start(root)
    root.mainloop()
