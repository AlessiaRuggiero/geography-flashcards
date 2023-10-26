import os
import sys
import tkinter as tk
from PIL import ImageTk, Image
from random import randint
from math import floor

# Image.Resampling.LANCZOS

# Get absolute path to resource


def resource_path(relative_path):
    # Get absolute path to resource
    try:
        # Pyinstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# Color variables
BG_COLOR = 'white'
FONT_COLOR = 'turquoise4'

# BASE FLASHCARD TEMPLATE -------------------------------------------------------------------------------


class FlashcardSet:
    def __init__(self):
        self.topic = 'Study Set'
        self.total_flashcards = 0
        self.scored = 0
        self.missed = 0

    def hasBeenStudied(self):
        return True if len(self.flashcards) < 1 else False

    # Print flashcard study information onto flashcards
    def print_topic(self, frame):
        title = tk.Label(frame, text=self.topic, bg=BG_COLOR,
                         fg=FONT_COLOR, font=('Helvetica', 18, 'bold')).pack()

    def print_progress(self, frame):
        progress = len(self.flashcards)
        global progress_label
        progress_label = tk.Label(frame, text='Cards left: ' + str(progress), bg=BG_COLOR, fg=FONT_COLOR,
                                  font=('Helvetica', 14))
        progress_label.pack()

    def print_score(self, frame):
        global score_label
        score_label = tk.Label(frame, text='Scored: ' + str(self.scored) + '\t\tMissed: ' + str(self.missed),
                               bg=BG_COLOR, fg=FONT_COLOR, font=('Helvetica', 14))
        score_label.pack()

    def random_flash(self):
        self.selected = randint(0, len(self.flashcards) - 1)

    def flash_answer(self, user_input):
        if user_input.title() == self.current_flash:
            self.scored += 1
            self.flashcards.pop(self.selected)
            return True, ''
        else:
            self.missed += 1
            self.flashcards.pop(self.selected)
            return False, self.current_flash

    def get_final_score(self):
        return floor(self.scored / self.total_flashcards * 100)

# NORTH AMERICAN TEMPLATES --------------------------------------------------------------------


class NACountriesSet(FlashcardSet):
    def __init__(self):
        super().__init__()
        self.topic = 'North American Countries'
        self.flashcards = ['Canada', 'United States', 'Mexico', 'Greenland', 'Guatemala',
                           'Belize', 'El Salvador', 'Honduras', 'Nicaragua', 'Costa Rica', 'Panama']
        self.total_flashcards = len(self.flashcards)

    def get_flashcard(self, frame):
        self.random_flash()
        self.current_flash = self.flashcards[self.selected]
        global state_img
        state_img = ImageTk.Image.open(resource_path(
            'Sets/NACountries/' + self.current_flash + '.png'))
        #state_img = ImageTk.Image.open('./Sets/NACountries/' + self.current_flash + '.png')
        resized_img = state_img.resize((400, 225), Image.LANCZOS)
        state_img = ImageTk.PhotoImage(resized_img)
        state_img_label = tk.Label(frame, image=state_img)
        state_img_label.pack()

    def get_map(self, frame):
        global map_img1
        map_img1 = ImageTk.Image.open(resource_path(
            'Sets/NACountries/NATemplate-filled.png'))
        #map_img1 = ImageTk.Image.open('./Sets/NACountries/NATemplate-filled.png')
        resized_img = map_img1.resize((350, 170), Image.LANCZOS)
        map_img1 = ImageTk.PhotoImage(resized_img)
        map_img1_label = tk.Label(frame, image=map_img1)
        map_img1_label.pack()
        global map_img2
        map_img2 = ImageTk.Image.open(resource_path(
            'Sets/NACountries/CATemplate-filled.png'))
        #map_img2 = ImageTk.Image.open('./Sets/NACountries/CATemplate-filled.png')
        resized_img = map_img2.resize((350, 175), Image.LANCZOS)
        map_img2 = ImageTk.PhotoImage(resized_img)

        map_img2_label = tk.Label(frame, image=map_img2)
        map_img2_label.pack()


class NAFlagsSet(FlashcardSet):
    def __init__(self):
        super().__init__()
        self.topic = 'North American Flags'
        self.flashcards = ['Canada', 'United States of America', 'Mexico', 'Greenland', 'Guatemala',
                           'Belize', 'El Salvador', 'Honduras', 'Nicaragua', 'Costa Rica', 'Panama']
        self.total_flashcards = len(self.flashcards)

    def get_flashcard(self, frame):
        self.random_flash()
        self.current_flash = self.flashcards[self.selected]
        global state_img
        state_img = ImageTk.Image.open(resource_path(
            'Sets/NAFlags/' + self.current_flash + '.png'))
        #state_img = ImageTk.Image.open('./Sets/NAFlags/' + self.current_flash + '.png')
        resized_img = state_img.resize((400, 225), Image.LANCZOS)
        state_img = ImageTk.PhotoImage(resized_img)
        state_img_label = tk.Label(frame, image=state_img)
        state_img_label.pack(pady=15)

    def get_map(self, frame):
        global map_img
        map_img = ImageTk.Image.open(resource_path(
            'Sets/NAFlags/NATemplate-filled.png'))
        #map_img = ImageTk.Image.open('./Sets/NAFlags/NATemplate-filled.png')
        resized_img = map_img.resize((400, 300), Image.LANCZOS)
        map_img = ImageTk.PhotoImage(resized_img)
        map_img_label = tk.Label(frame, image=map_img)
        map_img_label.pack()

# SOUTH AMERICAN TEMPLATES --------------------------------------------------------------------


class SACountriesSet(FlashcardSet):
    def __init__(self):
        super().__init__()
        self.topic = 'South American Countries'
        self.flashcards = ['Colombia', 'Ecuador', 'Peru', 'Chile', 'Bolivia', 'Paraguay', 'Uruguay',
                           'Venezuela', 'Guyana', 'Suriname', 'French Guiana', 'Brazil', 'Argentina']
        self.total_flashcards = len(self.flashcards)

    def get_flashcard(self, frame):
        self.random_flash()
        self.current_flash = self.flashcards[self.selected]
        global state_img
        state_img = ImageTk.Image.open(resource_path(
            'Sets/SACountries/' + self.current_flash + '.png'))
        #state_img = ImageTk.Image.open('./Sets/SACountries/' + self.current_flash + '.png')
        resized_img = state_img.resize((360, 320), Image.LANCZOS)
        state_img = ImageTk.PhotoImage(resized_img)
        state_img_label = tk.Label(frame, image=state_img)
        state_img_label.pack()

    def get_map(self, frame):
        global map_img
        map_img = ImageTk.Image.open(resource_path(
            'Sets/SACountries/SATemplate-filled.png'))
        #map_img = ImageTk.Image.open('./Sets/SACountries/SATemplate-filled.png')
        resized_img = map_img.resize((360, 320), Image.LANCZOS)
        map_img = ImageTk.PhotoImage(resized_img)
        map_img_label = tk.Label(frame, image=map_img)
        map_img_label.pack()


class SAFlagsSet(FlashcardSet):
    def __init__(self):
        super().__init__()
        self.topic = 'South American Flags'
        self.flashcards = ['Colombia', 'Ecuador', 'Peru', 'Chile', 'Bolivia', 'Paraguay', 'Uruguay',
                           'Venezuela', 'Guyana', 'Suriname', 'French Guiana', 'Brazil', 'Argentina']
        self.total_flashcards = len(self.flashcards)

    def get_flashcard(self, frame):
        self.random_flash()
        self.current_flash = self.flashcards[self.selected]
        global state_img
        state_img = ImageTk.Image.open(resource_path(
            'Sets/SAFlags/' + self.current_flash + '.png'))
        #state_img = ImageTk.Image.open('./Sets/SAFlags/' + self.current_flash + '.png')
        resized_img = state_img.resize((400, 225), Image.LANCZOS)
        state_img = ImageTk.PhotoImage(resized_img)
        state_img_label = tk.Label(frame, image=state_img)
        state_img_label.pack(pady=15)

    def get_map(self, frame):
        global map_img
        map_img = ImageTk.Image.open(resource_path(
            'Sets/SAFlags/SATemplate-filled.png'))
        #map_img = ImageTk.Image.open('./Sets/SAFlags/SATemplate-filled.png')
        resized_img = map_img.resize((400, 300), Image.LANCZOS)
        map_img = ImageTk.PhotoImage(resized_img)
        map_img_label = tk.Label(frame, image=map_img)
        map_img_label.pack()

# CARIBBEAN TEMPLATES ------------------------------------------------------------------------


class CRNationsSet(FlashcardSet):
    def __init__(self):
        super().__init__()
        self.topic = 'Caribbean Nations'
        self.flashcards = ['Anguilla', 'Antigua and Barbuda', 'Aruba', 'Bahamas', 'Barbados',
                           'British Virgin Islands', 'Cayman Islands', 'Cuba', 'Curaçao', 'Dominica',
                           'Dominican Republic', 'Grenada', 'Guadeloupe', 'Haiti', 'Jamaica',
                           'Martinique', 'Montserrat', 'Puerto Rico', 'St Kitts and Nevis',
                           'St Lucia', 'St Vincent and the Grenadines', 'Trinidad and Tobago',
                           'Turcs and Caicos', 'US Virgin Islands']
        self.total_flashcards = len(self.flashcards)

    def get_flashcard(self, frame):
        self.random_flash()
        self.current_flash = self.flashcards[self.selected]
        global state_img
        state_img = ImageTk.Image.open(resource_path(
            'Sets/CRNations/' + self.current_flash + '.png'))
        #state_img = ImageTk.Image.open('./Sets/CRNations/' + self.current_flash + '.png')
        resized_img = state_img.resize((430, 304), Image.LANCZOS)
        state_img = ImageTk.PhotoImage(resized_img)
        state_img_label = tk.Label(frame, image=state_img)
        state_img_label.pack()

    def get_map(self, frame):
        global map_img
        map_img = ImageTk.Image.open(resource_path(
            'Sets/CRNations/CRTemplate-filled.png'))
        #map_img = ImageTk.Image.open('./Sets/CRNations/CRTemplate-filled.png')
        resized_img = map_img.resize((430, 304), Image.LANCZOS)
        map_img = ImageTk.PhotoImage(resized_img)
        map_img_label = tk.Label(frame, image=map_img)
        map_img_label.pack()
