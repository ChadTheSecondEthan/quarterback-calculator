import tkinter

from scoring_preference import ScoringPreference
from button_group import ButtonGroup
from scoreboard_gui import ScoreboardGUI
from reader import Reader

class RatingGUI:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Scoring Preferences")
        self.reader = Reader()

        self.preferences = [ScoringPreference(self.window, self.on_preference_delete)]
        self.buttons = ButtonGroup(self.window, 
            ["Calculate Ratings", "Add Preference", "Quit"], 
            [self.calculate_ratings, self.add_preference, self.window.destroy])

        self.pack()

        tkinter.mainloop()

    def calculate_ratings(self):
        ScoreboardGUI(self.reader.get_players(), self.preferences)
        self.window.destroy()

    def add_preference(self):
        self.preferences.append(ScoringPreference(self.window, self.on_preference_delete))
        self.pack()

    def pack(self):
        for preference in self.preferences:
            preference.pack()
        self.buttons.pack(side='bottom')

    def on_preference_delete(self, preference):
        self.preferences.remove(preference)
        preference.frame.destroy()

        self.pack()