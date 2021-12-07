import tkinter

# Ethan Fisher
# 11/18/2021
# defines a group of buttons on the same line

class ButtonGroup:
    def __init__(self, window, texts, commands):
        # create one frame to hold all buttons
        self.frame = tkinter.Frame(window)

        # create an array of buttons that are each given a text
        # and a command
        self.buttons = []
        for i in range(len(texts)):
            self.buttons.append(tkinter.Button(self.frame, text=texts[i], command=commands[i]))

    # pack each element to put them each on the same line
    def pack(self, side='left'):
        for button in self.buttons:
            button.pack(side='left')
        self.frame.pack(side=side)
