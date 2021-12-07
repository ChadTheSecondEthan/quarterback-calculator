import tkinter

# Ethan Fisher
# 11/18/2021
# defines a label and entry within a frame

class InputArea:
    def __init__(self, window, text):
        # create a frame, label, and entry field
        self.frame = tkinter.Frame(window)
        self.label = tkinter.Label(self.frame, text=text)
        self.entry = tkinter.Entry(self.frame)

    # pack each element to put them each on the same line
    def pack(self):
        self.label.pack(side='left')
        self.entry.pack(side='left')
        self.frame.pack()

    # returns the current value of the entry
    def get(self):
        return self.entry.get()
