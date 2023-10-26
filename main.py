from curses.ascii import NUL
from templates import *

set_selected = None

# DISPLAY MAIN MENU AND HANDLE SELECTION INPUT
def choose_set():
    hide_open_frames()
    main_frame.pack(fill='both', expand=True)
    title = tk.Label(main_frame, text="Choose a set to study", bg=BG_COLOR, fg=FONT_COLOR,
                     font=('Helvetica', 18, 'bold')).pack(pady=30)
        
    # Function to display menu selection
    def menu_selection():
        # Function to initialize the set selected
        def init_set(topic):
            global set_selected
            if topic == 1:
                set_selected = NACountriesSet()
            elif topic == 2:
                set_selected = NAFlagsSet()
            elif topic == 3:
                set_selected = SACountriesSet()
            elif topic == 4:
                set_selected = SAFlagsSet()
            elif topic == 5:
                set_selected = CRNationsSet()
            study_flashcard()
            
        
        # NORTH AMERICAN MAIN MENU SELECTIONS
        na_label = tk.Label(main_frame, text='North America\n-----------------------------------------------------------',
                        bg=BG_COLOR, fg=FONT_COLOR, font=('Helvetica', 14, 'bold')).pack(pady=2)
        na_countries_button = tk.Button(main_frame, width=30, height=2, text='North America - countries', fg=FONT_COLOR,
                                    command=lambda: init_set(1))
        na_countries_button.pack(pady=10)
        na_flags_button = tk.Button(main_frame, width=30, height=2, text='North America - flags', fg=FONT_COLOR,
                                command=lambda: init_set(2))
        na_flags_button.pack(pady=10)

        # SOUTH AMERICAN MAIN MENU SELECTIONS
        na_label = tk.Label(main_frame, text='South America\n-----------------------------------------------------------',
                        bg=BG_COLOR, fg=FONT_COLOR, font=('Helvetica', 14, 'bold')).pack(pady=2)
        sa_countries_button = tk.Button(main_frame, width=30, height=2, text='South America - countries', fg=FONT_COLOR,
                                    command=lambda: init_set(3))
        sa_countries_button.pack(pady=10)
        sa_flags_button = tk.Button(main_frame, width=30, height=2, text='South America - flags', fg=FONT_COLOR,
                                command=lambda: init_set(4))
        sa_flags_button.pack(pady=10)

        # CARRIBEAN MAIN MENU SELECTIONS
        cr_label = tk.Label(main_frame, text='The Caribbean\n-----------------------------------------------------------',
                        bg=BG_COLOR, fg=FONT_COLOR, font=('Helvetica', 14, 'bold')).pack(pady=2)
        cr_nations_button = tk.Button(main_frame, width=30, height=2, text='Carribean Nations', fg=FONT_COLOR,
                                  command=lambda: init_set(5))
        cr_nations_button.pack(pady=10)
    
    menu_selection()


def study_flashcard():
    if set_selected.hasBeenStudied():
        return performance()

    # Get flashcard
    hide_open_frames()
    flash_frame.pack(fill='both', expand=True)
    set_selected.print_topic(flash_frame)
    set_selected.print_progress(flash_frame)
    set_selected.print_score(flash_frame)
    set_selected.get_flashcard(flash_frame)

    # HANDLE ANSWER INPUT --------------------------------------------------------------------
    def check_input():
        correct, correct_input = set_selected.flash_answer(enter_input.get())
        if correct:
            global correct_response
            correct_response = tk.Label(flash_frame, text='Correct!', fg='green2', font=('Helvetica', 18, 'bold'))
            correct_response.pack(pady=5)
            correct_response.after(600, study_flashcard)
        else:
            global incorrect_response, correction
            incorrect_response = tk.Label(flash_frame, text='Wrong!', fg='red', font=('Helvetica', 18, 'bold')).pack(pady=5)
            correction = tk.Label(flash_frame, text='>>> '+correct_input+' <<<', fg='red',
                                   font=('Helvetica', 14, 'underline'))
            correction.pack()
            correction.after(1000, study_flashcard)

    # Input answer
    enter_input = tk.Entry(flash_frame, highlightthickness=4, highlightcolor="turquoise3", bd=0)
    enter_input.pack(pady=10)
    enter_input.focus_set()


    input_button = tk.Button(flash_frame, text='Enter', fg=FONT_COLOR, font=('Helvetica', 18), command=check_input)
    input_button.pack(pady=10)
    root.bind('<Return>', lambda event: check_input())

    # Skip current flashcard
    pass_button = tk.Button(flash_frame, text='Pass', fg=FONT_COLOR, font=('Helvetica', 18),
                            command=study_flashcard)
    pass_button.pack(pady=5)

    # Return to main menu
    return_button = tk.Button(flash_frame, text='Return to main menu', fg=FONT_COLOR,
                              font=('Helvetica', 10), command=choose_set)
    return_button.pack(pady=5)


def performance():
    # Get flashcard
    hide_open_frames()
    final_frame.pack(fill='both', expand=True)
    title = tk.Label(final_frame, text='Performance\n-----------------------------------------------------------',
                     bg=BG_COLOR, fg=FONT_COLOR, font=('Helvetica', 24, 'bold')).pack(pady=5)
    set_selected.print_topic(final_frame)
    set_selected.print_score(final_frame)
    set_selected.get_map(final_frame)

    # Get final score
    final_score = set_selected.get_final_score()
    final_score_label = tk.Label(final_frame, text='You got '+str(final_score)+'% correct.', fg=FONT_COLOR,
                                 font=('Helvetica', 14, 'bold')).pack(pady=10)

    # Prompt restudy
    study_again = tk.Button(final_frame, width=30, height=2, text='Continue studying', fg=FONT_COLOR,
                            command=choose_set)
    study_again.pack(pady=10)

def hide_open_frames():
    for widget in main_frame.winfo_children():
        widget.destroy()
    main_frame.pack_forget()

    for widget in flash_frame.winfo_children():
        widget.destroy()
    flash_frame.pack_forget()

    for widget in final_frame.winfo_children():
        widget.destroy()
    final_frame.pack_forget()


if __name__ == '__main__':
    # START PROGRAM
    root = tk.Tk()
    root.title('American Geography Flashcards')
    root.geometry('480x600+500+250')

    # FRAME CREATION
    main_frame = tk.Frame(root, bg=BG_COLOR, width=480, height=600)
    flash_frame = tk.Frame(root, bg=BG_COLOR, width=480, height=600)
    final_frame = tk.Frame(root, bg=BG_COLOR, width=480, height=600)

    choose_set()

root.mainloop()
