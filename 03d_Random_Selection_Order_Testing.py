
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
# General inspiration from "00_Compiled_Version_6.py"
# Structural inspiration for this program's testing is inspired by "00_Compiled_Version_6.py"

# Research done on random selection (for the file "03_Random_Selection.py") as follows: https://stackabuse.com/how-to-randomly-select-elements-from-a-list-in-python/,
# ... https://pynative.com/python-random-sample/, https://stackoverflow.com/questions/18449360/access-item-in-a-list-of-lists,
# ... https://www.tutorialspoint.com/generating-random-number-list-in-python, https://www.geeksforgeeks.org/randomly-select-elements-from-list-without-repetition-in-python/,
# ... https://stackoverflow.com/questions/55611388/how-to-use-a-list-as-a-class-variable-so-that-instance-object-arguments-are-ap, https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide,
# ... https://www.sololearn.com/Discuss/1774331/is-it-a-bad-practice-to-use-list-as-a-class-variable, https://www.geeksforgeeks.org/how-to-get-a-list-of-class-attributes-in-python/

# Start Class (with various portions taken from "01_Mystery_Box_Outline.py" and also "02_Converter_GUI.py")
class Start:
    def __init__(self, parent):

        # Number of questions variable setup (inspired by "00_Compiled_Version_6.py") [Other inspiration from: https://stackoverflow.com/questions/54345396/not-able-to-set-value-for-tk-stringvar-using-set-method,
        # ... https://www.geeksforgeeks.org/python-setting-and-retrieving-values-of-tkinter-variable/,
        # ... https://www.google.com/search?q=IntVar+Set+Missing+Variable&rlz=1C1GCEV_enNZ951NZ952&oq=IntVar+Set+Missing+Variable&aqs=chrome..69i57j33i160.10960j1j7&sourceid=chrome&ie=UTF-8&safe=active&ssui=on]
        self.question_amount = IntVar
        self.question_amount.set(0)

        # GUI to find starting balance and stakes from the user:
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Question Amount Entry Box (Row 0) (inspired by "00_Compiled_Version_6.py")
        self.question_amount_entry_box = Entry(self.start_frame, font="Arial 14 bold", width=10)
        self.question_amount_entry_box.grid(row=0)

        # Question Amount Button (Row 1) (inspired by "00_Compiled_Version_6.py")
        self.question_amount_button = Button(self.start_frame, font="Arial 14 bold", text="Enter question amount",
                                             command=self.check_question_amount)
        self.question_amount_button.grid(row=1)

        # Test Button (Row 2)
        self.push_me_button = Button(self.start_frame, text="Press This", command=self.to_game)
        self.push_me_button.grid(row=2, pady=50, padx=50)

    # Check Question Amount Function (inspired by "check_funds" from "00_Compiled_Version_6.py")
    def check_question_amount(self):

        question_quantity = self.question_amount_entry_box.get()

        try:

            question_quantity = int(question_quantity)

            if question_quantity < 1:

                print ("incorrect")
            
            else:

                print ("correct")
                print (question_quantity)

                # Set questions asked to amount entered by user
                self.question_amount.set(question_quantity)

        except ValueError:
            
            print ("error")

        print (self.question_amount)

    def to_game(self):

        question_quantity = self.question_amount_entry_box.get()

        Quiz(self, question_quantity)

        # Hide start up window
        self.start_frame.destroy()

# Quiz Class (From the file titled "02c_Quiz_GUI_List_Testing.py")
class Quiz:
    def __init__(self, partner, question_quantity):

        # Prints question amount for testing purposes
        print(self.question_quantity)
        
        # Defining user_answer variable
        self.user_answer = StringVar

        # Initialise question variable
        self.question = IntVar()

        # Set question variable to question amount entered by user at start of game
        # self.question.set(question_amount)

        # GUI Setup
        self.quiz_box = Toplevel()

        # If users press cross at top, the game quits
        self.quiz_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        # Defining Game Frame
        self.quiz_frame = Frame(self.quiz_box, padx=10, pady=10)
        self.quiz_frame.grid()

        # Question number label (Row 0)
        self.question_number_label = Label(self.quiz_frame, text="1/{}".format(self.question_amount), font="Arial 10 bold",
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
        # ... [Research on how to select from a list within a list: https://stackoverflow.com/questions/18449360/access-item-in-a-list-of-lists]
        # ... (This has also been inspired by the file named "00_Compiled_Version_5.py")
        self.fear_name_label = Label(self.quiz_frame, text="", font="Arial 25",
                                        padx=10, pady=10, justify=CENTER)
        self.fear_name_label.grid(row=2)

        # Question text [Part 2] (Row 3)
        self.question_text_part_two = Label(self.quiz_frame, text="represents a fear of...", font="Arial 15",
                                        padx=10, pady=10, justify=LEFT)
        self.question_text_part_two.grid(row=3)

        # Answers Frame Setup (Row 4) [From "00_Compiled_Version_6.py"] 
        # ... (Formatting in this frame has been designed from a diagram) [Some button formatting from "12g_Assembled_Program.py"]
        # ... (Portions of this button have been inspired by the file "00_Compiled_Version_6.py".)
        self.answers_frame = Frame(self.quiz_frame)
        self.answers_frame.grid(row=4, pady=10, padx=10)

        # Answer Option 1 Button (Row 0, Column 0) [From "00_Compiled_Version_6.py"]
        # ... (Some inspiration taken from "https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list")
        self.answer_option_one_button = Button(self.answers_frame, font="Arial 10", width=10, text="", command=lambda: self.check_answer(0))
        self.answer_option_one_button.grid(row=0, column=0, pady=5, padx=10)

        # Answer Option 2 Button (Row 0, Column 1) [From "00_Compiled_Version_6.py"] 
        # ... (Some inspiration taken from "https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list")
        self.answer_option_two_button = Button(self.answers_frame, font="Arial 10", width=10, text="", command=lambda: self.check_answer(1))
        self.answer_option_two_button.grid(row=0, column=1, pady=5, padx=10)

        # Answer Option 3 Button (Row 1, Column 0) [From "00_Compiled_Version_6.py"]
        # ... (Some inspiration taken from "https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list")
        self.answer_option_three_button = Button(self.answers_frame, font="Arial 10", width=10, text="", command=lambda: self.check_answer(2))
        self.answer_option_three_button.grid(row=1, column=0, pady=5, padx=10)

        # Answer Option 4 Button (Row 1, Column 1) [From "00_Compiled_Version_6.py"]
        # ... (Some inspiration taken from "https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list")
        self.answer_option_four_button = Button(self.answers_frame, font="Arial 10", width=10, text="", command=lambda: self.check_answer(3))
        self.answer_option_four_button.grid(row=1, column=1, pady=5, padx=10)

        # Answers Submit Setup (Row 5) [From "00_Compiled_Version_6.py"] 
        # ... (Formatting in this frame has been designed from a diagram) 
        # ... [This setup has been adapted from the above frame]
        self.answers_submit_frame = Frame(self.quiz_frame)
        self.answers_submit_frame.grid(row=5, pady=10, padx=10)

        # Check Answer Button (Row 0, Column 0) [From "00_Compiled_Version_6.py"] (Adapted from above button template)
        self.check_answer_button = Button(self.answers_submit_frame, font="Arial 10", text="Check Answer", bg="yellow", state=DISABLED)
        self.check_answer_button.grid(row=0, column=0, pady=5, padx=10)

        # Next Question Button (Row 0, Column 1) [From "00_Compiled_Version_6.py"] (Adapted from above button template) [Partially inspired by "00_Compiled_Version_6.py".]
        # ... (Inspiration for button from: "https://stackoverflow.com/questions/57235726/how-can-i-assign-a-function-to-a-variable-without-running-it".)
        # ... [From the file "00_Compiled_Version_6.py".] (Inspired by the file "00_Compiled_Version_6.py")
        self.next_question_button = Button(self.answers_submit_frame, font="Arial 10", text="Begin Quiz", bg="green", command=self.question_randomising)
        self.next_question_button.grid(row=0, column=1, pady=5, padx=10)

        # Answer Label (Row 6)
        self.answer_label = Label(self.quiz_frame, font="Arial 10", text="", pady=10, padx=5)
        self.answer_label.grid(row=6)

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

    # Question randomising function
    def question_randomising(self):

        # Disables Check Answer button until first question is asked (from "00_Compiled_Version_6.py")
        self.check_answer_button.config(state=DISABLED)
                        
        # Disables Next Question button until answer is checked (from "00_Compiled_Version_6.py")
        self.next_question_button.config(state=DISABLED)

        # Changes Begin Quiz button to Next Question button
        self.next_question_button.config(text="Next Question")

        # Template for importing .csv files from "Data to Fish" at the following link: https://datatofish.com/import-csv-file-python-using-pandas/.
        # ... Code in the List Testing version has been adapted from the shown link ("https://datatofish.com/import-csv-file-python-using-pandas/")
        # ... during later versions. (Other resources used include: https://datatofish.com/convert-pandas-dataframe-to-list/, and https://datatofish.com/import-csv-file-python-using-pandas/)

        # This defines the fear_list variable as the entire provided .csv file
        fear_data = pd.read_csv (r'C:\users\grocottk70790\OneDrive - Massey High School\COM301\91906_&_91907_Programming\03_Fear_Quiz_Assessment\fear_list.csv')   

        # The following expands on the above line(s) of code and is taken from the following link: https://datatofish.com/import-csv-file-python-using-pandas/.
        # ... Collumn names taken from provided .csv file [Prior research and inspiration taken from the following sites: "https://www.datacamp.com/community/tutorials/python-select-columns", 
        # ... https://cmdlinetips.com/2020/04/3-ways-to-select-one-or-more-columns-with-pandas/, https://www.kite.com/python/answers/how-to-get-select-elements-from-a-list-or-tuple-in-python].
        # ... (Collumn names taken from "fear_list.csv")
        df = pd.DataFrame(fear_data, columns= ['Name','Fear'])

        # Converts "Pandas DataFrame" to a list (from the following link: "https://datatofish.com/convert-pandas-dataframe-to-list/")
        df = df.values.tolist()

        # Prints the entirety of the fear_list variable
        # print (df)

        # Takes four distinct questions and answers from the list and merges them into one (1) list
        questions_sample = random.sample(df, 4)

        # Prints questions_sample (for testing purposes)
        print (questions_sample)

        # Defines correct question and answer from list
        correct_list = questions_sample[0]
        correct_question = correct_list[0]
        correct_answer = correct_list[1]

        # Changing Fear Name Label to correct answer
        self.fear_name_label.config(text=correct_question)

        # Rearranges list into randomised order (somewhat related to the following link: https://pynative.com/python-random-sample/):
        randomised_answers = random.sample(questions_sample, 4)

        # Prints the correct anwer variable for testing purposes
        print (correct_answer)

        # Enables Check Answer button until first question is asked (from "00_Compiled_Version_6.py")
        self.check_answer_button.config(state=NORMAL)

        # Configuring button text
        self.answer_option_one_button.config(text=randomised_answers[0][1])
        self.answer_option_two_button.config(text=randomised_answers[1][1])
        self.answer_option_three_button.config(text=randomised_answers[2][1])
        self.answer_option_four_button.config(text=randomised_answers[3][1])

        return randomised_answers

    # Answer Checking Function (with portions from the file "00_Compiled_Version_6.py".) 
    # ... [Reserch on passing variables between functions as follows: https://stackoverflow.com/questions/16043797/python-passing-variables-between-functions]
    # ... (Further information from "https://www.geekpills.com/operating-system/linux/python-passing-variable-between-functions")
    # ... [Further research at the following link: "https://www.semicolonworld.com/question/57240/python-passing-variables-between-functions".]
    # ... (Further research on get statements: "https://www.tutorialspoint.com/python3/dictionary_get.htm") [Inspiration also from "00_Compiled_Version_6.py"]

    # Answer checking function [From "03b_Random_Selection_Version_2_Recovered.py".] (Function formatting inspired by "12g_Assembled_Program.py")
    # ... [This is a general research link that may inspire the program: "https://zetcode.com/python/lambda/".]
    # ... (This respource aims to educate on command(s): "https://www.google.com/search?q=pythin+get+command&rlz=1C1GCEV_enNZ951NZ952&oq=pythin+get+command&aqs=chrome..69i57j0i13l9.6352j1j7&sourceid=chrome&ie=UTF-8&safe=active&ssui=on".)
    def check_answer(self, chosen_button):
        # Prints chosen button variable
        print (chosen_button)

        # If the chosen button variable is equal to 0, tell the user that they are correct.
        if chosen_button == 0:
            
            # Changes answer section to display a correct error message (configure section from "12g_Assembled_Program.py")
            self.answer_label.configure(text="Correct", fg="green")
        
        # If the chosen button variable is not equal to 0, tell the user that they are incorrect.
        else:
            
            # Changes answer section to display an incorrect error message (configure section from "12g_Assembled_Program.py")
            self.answer_label.configure(text="Incorrect", fg="red")

    # Answer checking function (Function formatting inspired by "12g_Assembled_Program.py") 
    # def check_answer(self, answer_choice):

    # Function to quit game
    def to_quit(self):

        # Destroys window
        root.destroy()

# Main Routine (edited from "02_Start_GUI.py")
if __name__ == "__main__":
    root = Tk()
    root.title("Fear Quiz")
    something = Start(root)
    root.mainloop()
