import tkinter

# Ethan Fisher
# 11/18/2021
# defines labels within a frame

class LabelGroup:
    def __init__(self, window, texts):
        # create one frame to hold all labels
        self.frame = tkinter.Frame(window)

        # create an array of labels and fill it with labels
        # each containing a text from the texts array
        self.labels = []
        for text in texts:
            self.labels.append(tkinter.Label(self.frame, text=text))

    # pack each element to put them each on the same line
    def pack(self):
        for label in self.labels:
            label.pack(side='left')
        self.frame.pack()
