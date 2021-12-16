import tkinter

from input_area import InputArea

ScoringOptions = [
    "Touchdowns",
    "Passing Yards",
    "Interceptions"
]

class ScoringPreference:
    def __init__(self, window, on_destroy):
        self.frame = tkinter.Frame(window, pady=10, padx=10)
        self.top = tkinter.Frame(self.frame)
        self.bottom = tkinter.Frame(self.frame)
        self.weight_input = InputArea(self.bottom, text="Preference Weight")

        self.top_label = tkinter.Label(self.top, text="Select Preference Type:")

        self.option = tkinter.StringVar()
        self.option.set(ScoringOptions[0])
        self.top_dropdown = tkinter.OptionMenu(self.top, self.option, *ScoringOptions)

        self.destroy_button = tkinter.Button(self.frame, text="Remove Preference", command=lambda: on_destroy(self))

    def pack(self):
        self.top_label.pack(side='left')
        self.top_dropdown.pack(side='right')
        self.top.pack()

        self.weight_input.pack()
        self.bottom.pack()

        self.destroy_button.pack(side='bottom')
        self.frame.pack()

    def get_weight(self):
        return self.weight_input.get()

    def get_type(self):
        return self.option.get()