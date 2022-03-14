import tkinter
from turtle import left


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # congifure the main window

        self.main_window.geometry("500x200")

        self.label1 = tkinter.Label(self.main_window, text="Hello World!")

        self.label2 = tkinter.Label(self.main_window, text="This is my GUI program.")

        self.label1.pack(side="top")
        self.label2.pack(side="bottom")

        tkinter.mainloop()


my_gui = MyGUI()

print("moving on......")