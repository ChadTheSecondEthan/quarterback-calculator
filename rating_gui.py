import tkinter
import threading

from scoring_preference import ScoringPreference
from button_group import ButtonGroup
from input_area import InputArea
from scoreboard_gui import ScoreboardGUI
from reader import Reader

class ReaderThread(threading.Thread):
    def __init__(self, thread_name, thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID
        self.reader = False

    def run(self):
        self.reader = Reader()

class RatingGUI:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Scoring Preferences")
        self.reader_thread = ReaderThread("Reader Thread", 0)
        self.reader_thread.start()

        self.preferences = [ScoringPreference(self.window, self.on_preference_delete)]
        self.num_displayed = InputArea(self.window, text="How many to display?")
        self.buttons = ButtonGroup(self.window, 
            ["Calculate Ratings", "Add Preference", "Quit"], 
            [self.calculate_ratings, self.add_preference, self.window.destroy])

        self.pack()

        tkinter.mainloop()

    def calculate_ratings(self):
        ScoreboardGUI(self.reader_thread.reader.get_players(), self.preferences, int(self.num_displayed.get()))
        self.window.destroy()

    def add_preference(self):
        self.preferences.append(ScoringPreference(self.window, self.on_preference_delete))
        self.pack()

    def pack(self):
        self.num_displayed.pack()
        for preference in self.preferences:
            preference.pack()
        self.buttons.pack(side='bottom')

    def on_preference_delete(self, preference):
        self.preferences.remove(preference)
        preference.frame.destroy()

        self.pack()