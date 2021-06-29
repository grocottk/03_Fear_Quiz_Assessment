# Initial Start GUI from "01_Start_GUI.py"

# This file will become Component 1 of the "Fear Quiz Assessment".
# [Note: This file has now been edited on a new device, 
# ... so a new build of the code can now be marked as currently active]

# Import Statements as follows (from "01_Mystery_Box_Outline.py"):
from tkinter import *
import random
from functools import partial  # This prevents unwanted windows from opening
import \
    pandas as pd  # This import statement is from the template at the following link: https://datatofish.com/import-csv-file-python-using-pandas/


# The majority of the below code is from the program known as "05_Game_Playable.py"
# General inspiration from "00_Compiled_Version_6.py"
# Structural inspiration for this program's testing is inspired by "00_Compiled_Version_6.py"

# Research done on random selection (for the file "03_Random_Selection.py") as follows: https://stackabuse.com/how-to-randomly-select-elements-from-a-list-in-python/,
# ... https://pynative.com/python-random-sample/, https://stackoverflow.com/questions/18449360/access-item-in-a-list-of-lists,
# ... https://www.tutorialspoint.com/generating-random-number-list-in-python, https://www.geeksforgeeks.org/randomly-select-elements-from-list-without-repetition-in-python/,
# ... https://stackoverflow.com/questions/55611388/how-to-use-a-list-as-a-class-variable-so-that-instance-object-arguments-are-ap, https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide,
# ... https://www.sololearn.com/Discuss/1774331/is-it-a-bad-practice-to-use-list-as-a-class-variable, https://www.geeksforgeeks.org/how-to-get-a-list-of-class-attributes-in-python/

# Start Class (with various portions taken from "01_Mystery_Box_Outline.py" and also "02_Converter_GUI.py") [From "01_Start_GUI.py"]
class Start:
    def __init__(self, parent):

        # Initialising Start Frame (from "01_Mystery_Box_Outline.py")
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Defining question_amount variable
        self.question_amount = IntVar()
        self.question_amount.set(0)

        # Start Heading (Row 0)
        self.quiz_heading_label = Label(self.start_frame, text="Fear Quiz", font="Arial 25 bold", justify=CENTER,
                                        padx=10, pady=10)
        self.quiz_heading_label.grid(row=0)

        # Start Instructions (Row 1)
        self.start_instructions = Label(self.start_frame,
                                        text="Please enter the number of questions that you would like to answer in the box below.",
                                        font="Arial 10 italic", justify=LEFT, padx=10, pady=10, wrap=350)
        self.start_instructions.grid(row=1)

        # Number Entry Box (Row 2) [from "01_Mystery_Box_Outline.py"]
        self.number_entry_box = Entry(self.start_frame, width=50)
        self.number_entry_box.grid(row=2)

        # Start Error Message Area (Row 3)
        self.start_error_message_area = Label(self.start_frame, font="Arial 10", text="")
        self.start_error_message_area.grid(row=3)

        # Start Buttons Frame (Row 4) [inspired by "08b_Game_Export_GUI_Version_2.py" and "05_Game_Playable.py"]
        self.start_buttons_frame = Frame(pady=15)
        self.start_buttons_frame.grid(row=4)

        # Help Button (Row 0, Column 0)
        self.help_button = Button(self.start_buttons_frame, text="Help", font="Arial 10", pady=5, padx=10, bg="orange",
                                  command=self.to_help_from_start)
        self.help_button.grid(row=0, column=0, padx=5)

        # Check Questions Number Button (Row 0, Column 1)
        self.check_questions_number_button = Button(self.start_buttons_frame, text="Check Questions Number",
                                                    font="Arial 10", pady=5, padx=10, bg="pink",
                                                    command=self.check_question_amount)
        self.check_questions_number_button.grid(row=0, column=1, padx=5)

        # Start Button (Row 1, Column 0) [Button Spanning research at the following links:
        # ... https://www.google.com/search?q=How+to+span+across+columns+in+tkinter&rlz=1C1GCEV_enNZ951NZ952&oq=How+to+span+across+columns+in+tkinter&aqs=chrome..69i57j33i22i29i30l2.12096j1j7&sourceid=chrome&ie=UTF-8&safe=active&ssui=on,
        # ... https://stackoverflow.com/questions/44659879/ttk-button-span-multiple-columns]
        self.start_button = Button(self.start_buttons_frame, text="Start", font="Arial 10", pady=5, padx=10, bg="green",
                                   width=25,
                                   command=self.to_quiz, state=DISABLED)
        self.start_button.grid(row=1, column=0, columnspan=2, pady=5)

    # Question Amount Checking (inspired by "02_Start_GUI.py", specifically the segement titled "check_funds",
    # ... and "12g_Assembled_Program.py")
    def check_question_amount(self):

        # Get[s] initial data, and defines the question_amount_check variable as the number entry box entry
        question_amount_check = self.number_entry_box.get()

        # Sets initial variables, including background colour and error checking
        error_background = "pink"

        # This defines the has_errors variable, and sets it as "no"
        has_errors = "no"

        # Try the following
        try:

            # The user_question_amount becomes an integer
            question_amount_check = int(question_amount_check)

            # If the question amount is less than 1, give an error message
            if question_amount_check < 1:
                has_errors = "yes"
                error_feedback = "Sorry, the lowest number of questions that you can be asked is 1."

            # If the question amount is more than 113, give an error message
            elif question_amount_check > 113:
                has_errors = "yes"
                error_feedback = "Sorry, the highest number of questions that you can be asked is 113."

        # If a value error is present, tell the user that they have an error
        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a whole number between 1 and 113"

        # If the entry has an error, tell the user
        if has_errors == "yes":

            # If errors are present, change the error area
            self.start_error_message_area.config(bg=error_background, text=error_feedback)

        # If no errors are present, tell the user and continue
        else:

            # If no errors are present, tell the user that their answer is valid
            self.start_error_message_area.config(bg="lime", text="This is a valid number of questions")

            # Set total questions to the question_amount variable
            self.question_amount.set(question_amount_check)

            # Sets start button to a normal state
            self.start_button.config(state=NORMAL)

    # Defining the to_quiz function
    def to_quiz(self):

        # Gets question amount from entry box (from "00_Compiled_Version_6.py")
        question_amount = self.number_entry_box.get()

        # Prints the question_amount for testing
        # print (question_amount)

        # Sends variables to Quiz segmnent
        Quiz(self, question_amount)

        # Hide start up window
        self.start_frame.destroy()

        # Destroys start buttons frame
        self.start_buttons_frame.destroy()

    # Defining to_help function (inspired by the "to_quiz" function)
    def to_help_from_start(self):

        # Prints "functional" to test and see whether the function has been called and is functional
        # print("functional")

        # Sends the user to the health class window
        Help(self)

        # Destroys start window
        self.start_frame.destroy()

        # Destroys the frame of the start buttons (inspired by the "to_quiz" function)
        self.start_buttons_frame.destroy()


# Quiz Class (From the file titled "02c_Quiz_GUI_List_Testing.py") [This segment also takes inspiration from the file "00_Compiled_Version_6.py"]
class Quiz:
    def __init__(self, partner, question_amount):

        # Converts the question_amount_check into a variable
        question_amount = int(question_amount)

        # Initialise the question number variable
        self.question_number = IntVar()

        # Sets the question number to one (1) at the beginning of the quiz
        self.question_number.set(0)

        # The total questions asked
        # total_questions_asked_label = self.question_number

        # The total asked questions label becomes an integer
        # total_questions_asked_label = int(total_questions_asked_label)

        # Initialise the number of questions variable
        # self.number_of_questions = IntVar()

        # Sets the question number variable to the question amount stated in the start section (Resarch done includes the following:
        # https://www.google.com/search?q=.set+command+missing+1+value+in+python&rlz=1C1GCEV_enNZ951NZ952&oq=.set+command+missing+1+value+in+python&aqs=chrome..69i57.15571j0j7&sourceid=chrome&ie=UTF-8&safe=active&ssui=on,
        # https://stackoverflow.com/questions/38170566/python-typeerror-set-missing-1-required-positional-argument-value)
        # self.number_of_questions.set(question_amount)

        # Defining statistics list(s) (inspired by "00_Compiled_Version_6.py")
        # quiz_statistics_list = [question_amount, question_amount]

        # Prints the question_amount for testing
        # print (question_amount)

        # Defining correct_answer variable
        self.correct_answer = StringVar()

        # Defining correct_answer_count variable
        self.correct_answer_count = IntVar()

        # Sets the number of correct answers answered to zero (0)
        self.correct_answer_count.set(0)

        # Initialise question variable
        # self.number_of_questions = IntVar()

        # Set question variable to question amount entered by user at start of the quiz
        # self.number_of_questions.set(self.question_amount_check)

        # GUI Setup
        self.quiz_box = Toplevel()

        # If users press cross at top, the quiz quits
        self.quiz_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        # Defining the Quiz Frame
        self.quiz_frame = Frame(self.quiz_box, padx=10, pady=10)
        self.quiz_frame.grid()

        # Question number label (Row 0)
        self.question_number_label = Label(self.quiz_frame, font="Arial 10 bold", padx=10, pady=2, justify=CENTER,
                                           text="0/{}".format(question_amount))
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
        # ... [The following link inspires the below button's functionality, and was used late in the quiz main functionality's trialing process:
        # ... https://stackoverflow.com/questions/26765218/get-the-text-of-a-button-widget]
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
        self.answer_option_one_button = Button(self.answers_frame, font="Arial 10", width=10, text="",
                                               command=lambda: self.check_answer(self.answer_option_one_button['text'],
                                                                                 question_amount), state=DISABLED)
        self.answer_option_one_button.grid(row=0, column=0, pady=5, padx=10)

        # Answer Option 2 Button (Row 0, Column 1) [From "00_Compiled_Version_6.py"] 
        # ... (Some inspiration taken from "https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list")
        self.answer_option_two_button = Button(self.answers_frame, font="Arial 10", width=10, text="",
                                               command=lambda: self.check_answer(self.answer_option_two_button['text'],
                                                                                 question_amount), state=DISABLED)
        self.answer_option_two_button.grid(row=0, column=1, pady=5, padx=10)

        # Answer Option 3 Button (Row 1, Column 0) [From "00_Compiled_Version_6.py"]
        # ... (Some inspiration taken from "https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list")
        self.answer_option_three_button = Button(self.answers_frame, font="Arial 10", width=10, text="",
                                                 command=lambda: self.check_answer(
                                                     self.answer_option_three_button['text'], question_amount), state=DISABLED)
        self.answer_option_three_button.grid(row=1, column=0, pady=5, padx=10)

        # Answer Option 4 Button (Row 1, Column 1) [From "00_Compiled_Version_6.py"]
        # ... (Some inspiration taken from "https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list")
        self.answer_option_four_button = Button(self.answers_frame, font="Arial 10", width=10, text="",
                                                command=lambda: self.check_answer(
                                                    self.answer_option_four_button['text'], question_amount), state=DISABLED)
        self.answer_option_four_button.grid(row=1, column=1, pady=5, padx=10)

        # Answers Submit Setup (Row 5) [From "00_Compiled_Version_6.py"] 
        # ... (Formatting in this frame has been designed from a diagram) 
        # ... [This setup has been adapted from the above frame]
        self.answers_submit_frame = Frame(self.quiz_frame)
        self.answers_submit_frame.grid(row=5, pady=10, padx=10)

        # Check Answer Button (Row 0, Column 0) [From "00_Compiled_Version_6.py"] (Adapted from above button template)
        # self.check_answer_button = Button(self.answers_submit_frame, font="Arial 10", text="Check Answer", bg="yellow", state=DISABLED)
        # self.check_answer_button.grid(row=0, column=0, pady=5, padx=10)

        # Next Question Button (Row 0, Column 0) [From "00_Compiled_Version_6.py"] (Adapted from above button template) [Partially inspired by "00_Compiled_Version_6.py".]
        # ... (Inspiration for button from: "https://stackoverflow.com/questions/57235726/how-can-i-assign-a-function-to-a-variable-without-running-it".)
        # ... [From the file "00_Compiled_Version_6.py".] (Inspired by the file "00_Compiled_Version_6.py")
        self.next_question_button = Button(self.answers_submit_frame, font="Arial 10", text="Begin Quiz", bg="green",
                                           command=self.question_randomising)
        self.next_question_button.grid(row=0, column=0, pady=5, padx=10)

        # Answer Label (Row 6)
        self.answer_label = Label(self.quiz_frame, font="Arial 10", text="", pady=10, padx=5)
        self.answer_label.grid(row=6)

        # Quiz Bottom Buttons Frame (Row 7) [inspired by "08b_Game_Export_GUI_Version_2.py" and "05_Game_Playable.py"]
        # ... (From "01_Start_GUI.py")
        self.quiz_bottom_buttons_frame = Frame(self.quiz_frame)
        self.quiz_bottom_buttons_frame.grid(row=7)

        # Quit Button (Row 0, Column 0) [Function from "05_Game_Playable.py"]
        self.quit_button = Button(self.quiz_bottom_buttons_frame, text="Quit", font="Arial 10", pady=5, padx=10,
                                  bg="red",
                                  command=self.to_quit)
        self.quit_button.grid(row=0, column=0, padx=10)

        # Help Button (Row 0, Column 1)
        self.help_button = Button(self.quiz_bottom_buttons_frame, text="Help", font="Arial 10", pady=5, padx=10,
                                  bg="orange", command=self.to_help_from_quiz)
        self.help_button.grid(row=0, column=1, padx=10)

    # Question randomising function
    def question_randomising(self):

        # Disables Next Question Button (inspired by parts of the "question_randomising" function in this file)
        # self.next_question_button.config(state=DISABLED)

        # Disables Check Answer button until first question is asked (from "00_Compiled_Version_6.py")
        # self.check_answer_button.config(state=DISABLED)

        # Disables Next Question button until answer is checked (from "00_Compiled_Version_6.py")
        # self.next_question_button.config(state=DISABLED)

        # Sets up question adding variable (inspired by the following links: https://stackoverflow.com/questions/19719577/add-tkinters-intvar-to-an-integer,
        # ... https://www.google.com/search?q=how+to+add+to+an+IntVar&rlz=1C1GCEV_enNZ951NZ952&oq=how+to+add+to+an+IntVar&aqs=chrome..69i57.9264j0j7&sourceid=chrome&ie=UTF-8&safe=active&ssui=on)
        question_adding = self.question_number.get()

        # Question adding to integer definition
        question_adding = int(question_adding)

        # Adding one (1) to the question adding variable [inspired by the following links: https://www.google.com/search?q=how+to+add+to+integer+variables+in+python&rlz=1C1GCEV_enNZ951NZ952&ei=t7TPYKvbCpKU4-EPzdGYuAI&oq=how+to+add+to+integer+variables+in+python&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEBYQHjIGCAAQFhAeOgcIABBHELADOgQIABBDOgQILhBDOgUIABCRAjoICAAQsQMQgwE6BQgAELEDOg4ILhCxAxCDARDHARCjAjoLCC4QsQMQxwEQowI6AggAOgUILhCxAzoLCC4QsQMQxwEQrwE6CAguEMcBEK8BOgsILhDHARCvARCTAjoCCC46CgguEMcBEK8BEAo6BAgAEA06BggAEA0QHjoICCEQFhAdEB5Q9oYKWJnSCmDO1wpoCXACeACAAfMBiAGzPpIBBjAuNDUuMZgBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=gws-wiz&ved=0ahUKEwjrkoC6lafxAhUSyjgGHc0oBicQ4dUDCBE&uact=5&safe=active&ssui=on,
        # ... https://stackoverflow.com/questions/18893445/adding-1-to-a-variable-inside-a-function/18893522]
        question_adding = question_adding + 1

        # Sets question_number variable to already defined question_number variable
        self.question_number.set(question_adding)

        # Adds 1 to question_number variable
        # self.question_number.set(self.question_number + 1)

        # Changes Begin Quiz button to Next Question button
        self.next_question_button.config(text="Next Question")

        # Template for importing .csv files from "Data to Fish" at the following link: https://datatofish.com/import-csv-file-python-using-pandas/.
        # ... Code in the List Testing version has been adapted from the shown link ("https://datatofish.com/import-csv-file-python-using-pandas/")
        # ... during later versions. (Other resources used include: https://datatofish.com/convert-pandas-dataframe-to-list/, and https://datatofish.com/import-csv-file-python-using-pandas/)

        # This defines the fear_list variable as the entire provided .csv file
        fear_data = pd.read_csv(
            r'C:\users\grocottk70790\OneDrive - Massey High School\COM301\91906_&_91907_Programming\03_Fear_Quiz_Assessment\fear_list.csv')

        # The following expands on the above line(s) of code and is taken from the following link: https://datatofish.com/import-csv-file-python-using-pandas/.
        # ... Collumn names taken from provided .csv file [Prior research and inspiration taken from the following sites: "https://www.datacamp.com/community/tutorials/python-select-columns", 
        # ... https://cmdlinetips.com/2020/04/3-ways-to-select-one-or-more-columns-with-pandas/, https://www.kite.com/python/answers/how-to-get-select-elements-from-a-list-or-tuple-in-python].
        # ... (Collumn names taken from "fear_list.csv")
        df = pd.DataFrame(fear_data, columns=['Name', 'Fear'])

        # Converts "Pandas DataFrame" to a list (from the following link: "https://datatofish.com/convert-pandas-dataframe-to-list/")
        df = df.values.tolist()

        # Prints the entirety of the fear_list variable
        # print (df)

        # Takes four distinct questions and answers from the list and merges them into one (1) list
        questions_sample = random.sample(df, 4)

        # Prints questions_sample (for testing purposes)
        # print(questions_sample)

        # Defines correct question and answer from list
        correct_list = questions_sample[0]
        correct_question = correct_list[0]
        # self.correct_answer = correct_list[1]

        self.correct_answer.set(correct_list[1])

        # Changing Fear Name Label to correct answer
        self.fear_name_label.config(text=correct_question)

        # Rearranges list into randomised order (somewhat related to the following link: https://pynative.com/python-random-sample/):
        randomised_answers = random.sample(questions_sample, 4)

        # Disables Check Answer button until first question is asked (from "00_Compiled_Version_6.py")
        self.next_question_button.config(state=DISABLED)

        # Configuring button text, and enabling buttons for answering (from "04b_Statistic_Gathering_Loop.py")
        self.answer_option_one_button.config(text=randomised_answers[0][1], state=NORMAL)
        self.answer_option_two_button.config(text=randomised_answers[1][1], state=NORMAL)
        self.answer_option_three_button.config(text=randomised_answers[2][1], state=NORMAL)
        self.answer_option_four_button.config(text=randomised_answers[3][1], state=NORMAL)

        # Enables Next Question Button (inspired by parts of the "question_randomising" function in this file)
        # ... [Inspired by the disabling code above]
        # self.next_question_button.config(state=NORMAL)

    # Answer Checking Function (with portions from the file "00_Compiled_Version_6.py".) 
    # ... [Reserch on passing variables between functions as follows: https://stackoverflow.com/questions/16043797/python-passing-variables-between-functions]
    # ... (Further information from "https://www.geekpills.com/operating-system/linux/python-passing-variable-between-functions")
    # ... [Further research at the following link: "https://www.semicolonworld.com/question/57240/python-passing-variables-between-functions".]
    # ... (Further research on get statements: "https://www.tutorialspoint.com/python3/dictionary_get.htm") [Inspiration also from "00_Compiled_Version_6.py"]

    # Answer checking function [From "03b_Random_Selection_Version_2_Recovered.py".] (Function formatting inspired by "12g_Assembled_Program.py")
    # ... [This is a general research link that may inspire the program: "https://zetcode.com/python/lambda/".]
    # ... (This respource aims to educate on command(s): "https://www.google.com/search?q=pythin+get+command&rlz=1C1GCEV_enNZ951NZ952&oq=pythin+get+command&aqs=chrome..69i57j0i13l9.6352j1j7&sourceid=chrome&ie=UTF-8&safe=active&ssui=on".)
    def check_answer(self, chosen_button, question_amount):

        # Prints chosen button variable
        # print (chosen_button)

        # Defines the total_questions_asked variable as the question_number variable
        total_questions_asked = self.question_number.get()

        # Sets up the correct answer amount variable
        correct_answer_amount = self.correct_answer_count.get()

        # Sets correct answer as correct answer check variable for analysis
        correct_answer_check = self.correct_answer.get()

        # Prints correct answer check variable for testing
        # print(correct_answer_check)

        # If the total questions asked variable is greater than or equal to the question amount variable,
        # ... update the answer label, and end the quiz.
        if total_questions_asked >= question_amount:

            # Tells the user that they have finished the quiz once all questions have been asked
            self.answer_label.config(
                text="You have finished the quiz with {} of {} questions correct".format(correct_answer_amount,
                                                                                         total_questions_asked),
                fg="black")

            # Disables the next question button if the designated number of questions have been asked
            # ... (This button is currently not functional in its intended purpose, and will hopefully be fixed
            # ... in future versions) [Inspiration possibly partially taken from "next_question_button" variable]
            # ... (Inspired by above question buttons)
            self.next_question_button.configure(text="View Statistics", bg="orange",
                                                command=lambda: self.to_statistics(question_amount, correct_answer_amount))

            # Disables the answer buttons (inspired by "04b_Statistic_Gathering_Loop.py"
            # ... and other portions of this function)
            self.answer_option_one_button.config(state=DISABLED)
            self.answer_option_two_button.config(state=DISABLED)
            self.answer_option_three_button.config(state=DISABLED)
            self.answer_option_four_button.config(state=DISABLED)

        # If the total questions asked is not the same as the question amount, allow the user to continue,
        # ... checking to see if their answer is correct
        else:

            # If the chosen button variable is equal to 0, tell the user that they are correct.
            if chosen_button == correct_answer_check:

                # Adds one (1) to correct answer amount
                correct_answer_amount = correct_answer_amount + 1

                # Changes answer section to display a correct message and amount correct (configure section from "12g_Assembled_Program.py")
                self.answer_label.configure(
                    text="Correct, you have entered {} correct answer(s)".format(correct_answer_amount), fg="green")

            # If the chosen button variable is not equal to 0, tell the user that they are incorrect.
            else:

                # Changes answer section to display an incorrect error message (configure section from "12g_Assembled_Program.py")
                self.answer_label.configure(
                    text="Incorrect, you have entered {} correct answer(s)".format(correct_answer_amount), fg="red")

        # Sets the question number to the total questions asked
        # self.question_number.set(total_questions_asked)

        # Prints correct answer amount for testing purposes
        # print(correct_answer_amount)

        # Sets the wider correct answer count variable to the correct answer amount variable
        # ... (inspired by a part of this program's function known as "check_question_amount")
        self.correct_answer_count.set(correct_answer_amount)

        # Enables Check Answer button after question is asked (from "00_Compiled_Version_6.py") [Inspired by above "question_randomising" function]
        self.next_question_button.config(state=NORMAL)

        # Disables answer buttons (from "04b_Statistic_Gathering_Loop.py")
        self.answer_option_one_button.config(state=DISABLED)
        self.answer_option_two_button.config(state=DISABLED)
        self.answer_option_three_button.config(state=DISABLED)
        self.answer_option_four_button.config(state=DISABLED)

        # Sets question number labels to relevant numbers
        self.question_number_label.configure(text="{}/{}".format(total_questions_asked, question_amount))

    # Answer checking function (Function formatting inspired by "12g_Assembled_Program.py") 
    # def check_answer(self, answer_choice):

    # Function to quit quiz
    def to_quit(self):

        # Destroys window
        root.destroy()

    # Calls statistics window (inspired by "00_Compiled_Version_6.py")
    def to_statistics(self, question_amount, correct_answer_amount):

        # Calls Statistics window (parts originally from above code segment)
        Statistics(self, question_amount, correct_answer_amount)

        # Destroys quiz window (inspired by the "to_quiz" function)
        self.quiz_box.destroy()

    # Creating a function that opens the help window from the quiz window (inspired by the "to_help_from_start"
    # ... function) (inspired by the "to_quiz" function)
    def to_help_from_quiz(self):

        # Prints "functional" to test and see whether the function has been called and is functional
        # print("functional")

        # Sends the user to the "Help" window
        Help(self)

        # Destroys quiz frame
        self.quiz_frame.destroy()

        # Destroys quiz box (from the above segment of the "to_help_from_quiz" function.)
        self.quiz_box.destroy()

        # Destroys the frame of the start buttons (inspired by the "to_quiz" function)
        # self.start_buttons_frame.destroy()


# Statistics Class (setup  of class inspired by above classes)
class Statistics:
    def __init__(self, partner, question_amount, correct_answer_amount):

        # Gets question number total
        # question_number_total = question_amount

        # GUI Setup (from above class)
        self.statistics_box = Toplevel()

        # Creating the statistics frame (inspired by the "Quiz" segment) [frame name(s) replaced using replace function]
        self.statistics_frame = Frame(self.statistics_box, padx=10, pady=10)
        self.statistics_frame.grid()

        # Statistics Page Title (Row 0) [inspired by above classes]
        self.statistics_title_label = Label(self.statistics_frame, font="Arial 20 bold", text="Quiz Statistics")
        self.statistics_title_label.grid(row=0, padx=20, pady=10)

        # Total questions asked label (Row 1) [Inspired by above label(s) in this project]
        # ... (justify command inspired by "start_instructions")
        self.total_questions_asked = Label(self.statistics_frame, text="Total questions asked: {}"
                                           .format(question_amount), justify=LEFT)
        self.total_questions_asked.grid(row=1)

        # Number of correct answers label (Row 2) [Inspired by above label(s) in this project]
        # ... (justify command inspired by "start_instructions")
        self.correct_answers_number_label = Label(self.statistics_frame, text="Correct answers: {}"
                                                  .format(correct_answer_amount), justify=LEFT)
        self.correct_answers_number_label.grid(row=2)

        # Number of incorrect answers label (Row 3) [Inspired by above label(s) in this project]
        # ... (justify command inspired by "start_instructions")
        self.incorrect_answers_number_label = Label(self.statistics_frame, text="Incorrect answers: {}"
                                                    .format(question_amount - correct_answer_amount),
                                                    justify=LEFT)
        self.incorrect_answers_number_label.grid(row=3)

        # Correct answers ratio label (Row 4) [Inspired by above label(s) in this project]
        # ... (justify command inspired by "start_instructions")
        self.correct_answers_ratio_label = Label(self.statistics_frame,
                                                 text="Correct answers ratio (correct answers/total answers): {}/{}"
                                                 .format(correct_answer_amount, question_amount), justify=LEFT)
        self.correct_answers_ratio_label.grid(row=4)

        # Correct answers percentage label (Row 5) [Inspired by above label(s) in this project]
        self.correct_answers_percentage_label = Label(self.statistics_frame,
                                                      text="{:.2f}%"
                                                      .format(correct_answer_amount / question_amount * 100),
                                                      font="Arial 60 bold", padx=5, pady=2)
        self.correct_answers_percentage_label.grid(row=5)

        # Correct answers percentage text label (Row 6) [Inspired by above label(s) in this project]
        # ... (structure inspired by above "correct_answers_percentage_label")
        self.correct_answers_percentage_text_label = Label(self.statistics_frame,
                                                           text="of the answers that you have given are correct",
                                                           font="Arial 10 bold", padx=5)
        self.correct_answers_percentage_text_label.grid(row=6)

        # Statistics buttons frame (Row 7) [This has been inspired by the "quiz_bottom_buttons_frame"]
        # ... {[inspired by "08b_Game_Export_GUI_Version_2.py" and "05_Game_Playable.py"] (From "01_Start_GUI.py")}
        self.statistics_buttons_frame = Frame(self.statistics_frame)
        self.statistics_buttons_frame.grid(row=7, pady=20)

        # Dismiss Button (Row 0, Column 0) [Inspired by "statistics_buttons_frame" formatting]
        # ... (padding ispired by the "quit_button") [Inspired by "00_Compiled_Version_6.py"]
        self.statistics_dismiss_button = Button(self.statistics_buttons_frame, text="Quit", bg="red", pady=5,
                                                padx=10, command=self.statistics_close)
        self.statistics_dismiss_button.grid(row=0, column=0, padx=10)

        # Export Button (Row 0, Column 1) [Inspired by "statistics_buttons_frame" formatting]
        # ... (inspired by above "statistics_dismiss_button") [padding inspired by the "quit_button"]
        # ... (inspired by the "statistics_dismiss_button" button)
        self.statistics_export_button = Button(self.statistics_buttons_frame, text="Export", bg="blue", pady=5,
                                               padx=10, command=self.to_export)
        self.statistics_export_button.grid(row=0, column=1, padx=10)

    # Statistics closing function (inspired by "00_Compiled_Version_6.py")
    def statistics_close(self):

        # Destroys statistics box
        self.statistics_box.destroy()

        # Destroys root
        root.destroy()

    # Defines a to_export function
    def to_export(self):

        # Prints a message stating that the function is functional once a button has been pressed.
        # print("functional")

        # Opens the export class (and/or window)
        Export(self)

        # Destroys the statistics frame (inspired by mention of the "statistics_frame")
        self.statistics_frame.destroy()

        # Destroys the statistics window (inspired by above code mentioning the "statistics_box")
        self.statistics_box.destroy()

# Help Class (inspired by the "Statistics" class)
class Help:
    def __init__(self, partner):

        # Prints the help_test variable for testing purposes
        # print(help_test)

        # Defining help_text variable (some mentioned names inspired by the "Start" and "Quiz" segments)
        help_text = "Welcome to the Fear Quiz, what follows is some basic help for this quiz, \n" \
                    "which will hopefully allow you to complete it to the best of your ability." \
                    "\n\n" \
                    "   1. Please begin by entering the number of questions that you would like to be \n" \
                    "       asked (between 1 and 113) into the provided text box in the start window. After this, \n" \
                    "       please check your entry with the 'Check Questions Number', and then once the answer \n" \
                    "       has been checked, you can press the start button." \
                    "\n\n" \
                    "   2. Once you are in in the quiz window itself, you can press the green 'Begin Quiz' button to \n" \
                    "       begin the quiz. To answer the question shown, you can press the button that you would like to \n" \
                    "       use as your answer. Once you have pressed this button, you will be told the result of your \n" \
                    "       guess (as in, whether it is correct or incorrect), as well as the number of questions that \n" \
                    "       you have correctly answered up until that point. After this, you can press the 'Next Question' \n" \
                    "       button to continue to the next question. The question counter at the top of the window will \n" \
                    "       allow you to have an idea of how far through the quiz you are." \
                    "\n\n" \
                    "   3. After you have completed the quiz, you can quit the quiz by pressing the 'Quit' button. \n" \
                    "       If you would like to view the statistics of your quiz, you can press the 'View Statistics' \n" \
                    "       button. While in this window, you can view a number of important statistics from your quiz. \n" \
                    "       After viewing these statistics, you can either press the 'Quit' button to quit the window(s), \n" \
                    "       or the 'Export' button to open the export window. Once in the export window, you will be able \n" \
                    "       to export the data that you have generated throughout the quiz." \
                    "\n\n" \
                    "Once you dismiss this help window, the start window will open again, in order for you to \n" \
                    "continue and/or begin your quiz. Good luck." \

        # Sets up GUI
        self.help_box = Toplevel()

        # Creating the help frame (inspired by the "Quiz" segment) [frame name(s) replaced using replace function]
        # ... (inspired by the "statistics_frame")
        self.help_frame = Frame(self.help_box, padx=10, pady=10)
        self.help_frame.grid()

        # Help heading label (Row 0) [inspired by above classes] (inspired by the "statistics_title_label")
        self.help_heading_label = Label(self.help_frame, font="Arial 20 bold", text="Fear Quiz Help")
        self.help_heading_label.grid(row=0, padx=20, pady=10)

        # Help text label (Row 1) [inspired by the "help_heading_label"]
        self.help_text_label = Label(self.help_frame, text=help_text, justify=LEFT)
        self.help_text_label.grid(row=1)

        # Help dismiss button (Row 2) [Inspired by the "Start" segment and some of the above formatting in the
        # ... "help_text_label" as an example]
        self.help_dismiss_button = Button(self.help_frame, text="Dismiss", font="Arial 10", pady=5, padx=10, bg="red",
                                          command=self.quit_to_start)
        self.help_dismiss_button.grid(row=2, padx=5, pady=10)

    # Defining a function that quits from the help window, back to the start window
    def quit_to_start(self):

        # Prints a message stating that the button is functional if the button is functional
        # print("functional")

        # Opens the start window
        Start(self)

        # Destroys the help window
        self.help_box.destroy()


# Export Class (inspired by the "Help" class, and the "Export" class in "00_Compiled_Version_6.py")
class Export:
    def __init__(self, partner):

        # Prints text that indicates that the window has been correctly mentioned
        print("functional")

        # Establishes the export box (inspired by "00_Compiled_Version_6.py") [inspired by "00_Compiled_Version_6.py"]
        self.export_box = Toplevel()

        # Sets up the export frame (inspired by "00_Compiled_Version_6.py")
        self.export_frame = Frame(self.export_box, width=500)
        self.export_frame.grid()

        # Export heading label (Row 0) [partially inspired by "00_Compiled_Version_6.py"]
        self.export_heading_label = Label(self.export_frame, text="Statistics Export", font="Arial 20 bold")
        self.export_heading_label.grid(row=0)


# Main Routine (edited from "02_Start_GUI.py")
if __name__ == "__main__":
    root = Tk()
    root.title("Fear Quiz")
    something = Start(root)
    root.mainloop()
