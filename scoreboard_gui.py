import tkinter

from label_group import LabelGroup

class ScoreboardGUI: 
    def __init__(self, players, preferences):
        self.window = tkinter.Tk()
        self.window.title("Players")
        self.labels = []

        for i in range(10):
            player = players[i]
            self.labels.append(LabelGroup(self.window, [player.__str__()]))

        self.pack()

        tkinter.mainloop()

    def pack(self):
        for label in self.labels:
            label.pack()
