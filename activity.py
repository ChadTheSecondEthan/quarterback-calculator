import tkinter

from input_area import InputArea

# Ethan Fisher
# 11/18/2021
# a class for an activity, which includes a name, hours per day, and a delete button

class Activity:
    def __init__(self, window, on_destroy):
        # create the frame and widgets that go inside
        self.frame = tkinter.Frame(window, pady=10)
        self.name_input = InputArea(self.frame, "Activity Name:")
        self.hours_input = InputArea(self.frame, "Hours per day:")
        self.delete_button = tkinter.Button(self.frame, text="Remove", command=self.delete)

        # remember the on_destroy function for when this activity is destroyed
        self.on_destroy = on_destroy

    # destroy the frame and call the on_destroy function
    def delete(self):
        self.frame.destroy()
        self.on_destroy(self)

    # pack each widget
    def pack(self):
        self.name_input.pack()
        self.hours_input.pack()
        self.delete_button.pack(side='bottom')
        self.frame.pack()

    # returns the value of the name entry
    def get_name(self):
        return self.name_input.get()

    # returns the number of hours per day
    def get_hours(self):
        return float(self.hours_input.get())