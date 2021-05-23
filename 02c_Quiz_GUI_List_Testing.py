
# Initial Start GUI from "01_Start_GUI.py"

# This file will become Component 1 of the "Fear Quiz Assessment".
# [Note: This file has now been edited on a new device, 
# ... so a new build of the code can now be marked as currently active]

# Import Statements as follows (from "01_Mystery_Box_Outline.py"):
from tkinter import *
import random
from functools import partial # This prevents unwanted windows from opening
import pandas as pd # This import statement is from the template at the following link: https://datatofish.com/import-csv-file-python-using-pandas/

# The majority of the below code is from the program known as "05_Game_Playable.py"

# Start Class (with various portions taken from "01_Mystery_Box_Outline.py" and also "02_Converter_GUI.py")
class Start:
    def __init__(self, parent):

        # GUI to find starting balance and stakes from the user:
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Test Button (Row 0)
        self.push_me_button = Button(self.start_frame, text="Press This", command=self.to_game)
        self.push_me_button.grid(row=0, pady=50, padx=50)

    def to_game(self):

        # Set question amount to 20
        question_amount = 20

        Quiz(self, question_amount)

        # Hide start up window
        self.start_frame.destroy()

class Quiz:
    def __init__(self, partner, question_amount):

        print(question_amount)
            
        # Template for importing .csv files from "Data to Fish" at the following link: https://datatofish.com/import-csv-file-python-using-pandas/.
        # ... Code in the List Testing version has been adapted from the shown link ("https://datatofish.com/import-csv-file-python-using-pandas/")
        # ... during later versions.

        # This defines the fear_list variable as the entire provided .csv file
        fear_data = pd.read_csv (r'C:\users\grocottk70790\OneDrive - Massey High School\COM301\91906_&_91907_Programming\03_Fear_Quiz_Assessment\fear_list.csv')   

        # The following expands on the above line(s) of code and is taken from the following link: https://datatofish.com/import-csv-file-python-using-pandas/.
        # ... Collumn names taken from provided .csv file [Prior research and inspiration taken from the following sites: "https://www.datacamp.com/community/tutorials/python-select-columns", 
        # ... https://cmdlinetips.com/2020/04/3-ways-to-select-one-or-more-columns-with-pandas/, https://www.kite.com/python/answers/how-to-get-select-elements-from-a-list-or-tuple-in-python]
        df = pd.DataFrame(fear_data, columns= ['Name','Fear'])

        # Converts "Pandas DataFrame" to a list (from the following link: "https://datatofish.com/convert-pandas-dataframe-to-list/")
        df = df.values.tolist()

        # Prints the entirety of the fear_list variable
        print (df)

        # Chooses a random selection from the given list, and stores it as the "question_choice" variable (From "https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list")
        question_choice = (random.choice(df))

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
                                padx=10, pady=2, justify=CENTER)
        self.question_number_label.grid(row=0)

        # Question text [Part 1] (Row 1)
        self.question_text_part_one = Label(self.quiz_frame, text="The word...", font="Arial 15",
                                        padx=10, pady=10, justify=LEFT)
        self.question_text_part_one.grid(row=1)

        # Fear Name (Row 2) [Inspiration taken from the following sites: "https://www.datacamp.com/community/tutorials/python-select-columns", 
        # ... https://cmdlinetips.com/2020/04/3-ways-to-select-one-or-more-columns-with-pandas/, https://www.kite.com/python/answers/how-to-get-select-elements-from-a-list-or-tuple-in-python]
        # ... (Formatting inspiration taken from the following link(s): https://www.kite.com/python/answers/how-to-get-select-elements-from-a-list-or-tuple-in-python,
        # ... https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list)
        self.fear_name_label = Label(self.quiz_frame, text="{}".format(question_choice[0]), font="Arial 25",
                                        padx=10, pady=10, justify=CENTER)
        self.fear_name_label.grid(row=2)

        # Question text [Part 2] (Row 3)
        self.question_text_part_two = Label(self.quiz_frame, text="represents a fear of...", font="Arial 15",
                                        padx=10, pady=10, justify=LEFT)
        self.question_text_part_two.grid(row=3)

        # Answers Frame Setup (Row 4) [From "00_Compiled_Version_6.py"] 
        # ... (Formatting in this frame has been designed from a diagram)
        self.answers_frame = Frame(self.quiz_frame)
        self.answers_frame.grid(row=4, pady=10, padx=10)

        # Answer Option 1 Button (Row 0, Column 0) [From "00_Compiled_Version_6.py"] (Some inspiration taken from "https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list")
        self.answer_option_one_button = Button(self.answers_frame, font="Arial 10", text="{}".format(question_choice[1]))
        self.answer_option_one_button.grid(row=0, column=0, pady=5, padx=10)

        # Answer Option 2 Button (Row 0, Column 1) [From "00_Compiled_Version_6.py"]
        self.answer_option_two_button = Button(self.answers_frame, font="Arial 10", text="[Option 2]")
        self.answer_option_two_button.grid(row=0, column=1, pady=5, padx=10)

        # Answer Option 3 Button (Row 1, Column 0) [From "00_Compiled_Version_6.py"]
        self.answer_option_three_button = Button(self.answers_frame, font="Arial 10", text="[Option 3]")
        self.answer_option_three_button.grid(row=1, column=0, pady=5, padx=10)

        # Answer Option 4 Button (Row 1, Column 1) [From "00_Compiled_Version_6.py"]
        self.answer_option_four_button = Button(self.answers_frame, font="Arial 10", text="[Option 4]")
        self.answer_option_four_button.grid(row=1, column=1, pady=5, padx=10)

        # Answers Submit Setup (Row 5) [From "00_Compiled_Version_6.py"] 
        # ... (Formatting in this frame has been designed from a diagram) 
        # ... [This setup has been adapted from the above frame]
        self.answers_submit_frame = Frame(self.quiz_frame)
        self.answers_submit_frame.grid(row=5, pady=10, padx=10)

        # Check Answer Button (Row 0, Column 0) [From "00_Compiled_Version_6.py"] (Adapted from above button template)
        self.check_answer_button = Button(self.answers_submit_frame, font="Arial 10", text="Check Answer", bg="yellow")
        self.check_answer_button.grid(row=0, column=0, pady=5, padx=10)

        # Next Question Button (Row 0, Column 1) [From "00_Compiled_Version_6.py"] (Adapted from above button template)
        self.next_question_button = Button(self.answers_submit_frame, font="Arial 10", text="Next Question", bg="green")
        self.next_question_button.grid(row=0, column=1, pady=5, padx=10)

        # Statistics Summary Label (Row 6)
        self.statistics_summary_label = Label(self.quiz_frame, font="Arial 10", text="", pady=10, padx=5)
        self.statistics_summary_label.grid(row=6)

        # Quiz Bottom Buttons Frame (Row 7) [inspired by "08b_Game_Export_GUI_Version_2.py" and "05_Game_Playable.py"]
        # ... (From "01_Start_GUI.py")
        self.quiz_bottom_buttons_frame = Frame(self.quiz_frame)
        self.quiz_bottom_buttons_frame.grid(row=7)
        
        # Quit Button (Row 0, Column 0) [Function from "05_Game_Playable.py"]
        self.quit_button = Button(self.quiz_bottom_buttons_frame, text="Quit", font="Arial 10", pady=5, padx=10, bg="red",
                                command=self.to_quit)
        self.quit_button.grid(row=0, column=0, padx=10)

        # Help Button (Row 0, Column 1)
        self.help_button = Button(self.quiz_bottom_buttons_frame, text="Help", font="Arial 10", pady=5, padx=10, bg="orange")
        self.help_button.grid(row=0, column=1, padx=10)

    def to_quit(self):

        root.destroy()

# Main Routine (edited from "02_Start_GUI.py")
if __name__ == "__main__":
    root = Tk()
    root.title("Fear Quiz")
    something = Start(root)
    root.mainloop()
