from cgitb import text
import tkinter
from turtle import left, width



class KiloConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("500x200")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(
            self.top_frame, text="Enter a distance in Kilometers:"
        )

        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side="left")

        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="top")

        self.calcbutton = tkinter.Button(
            self.main_window, text="Convert", command=self.convert
        )

        self.quit_button = tkinter.Button(
            self.main_window, text="Quit", command=self.main_window.destroy
        )

        self.calcbutton.pack(side="left")
        self.quit_button.pack(side="right")

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())

        miles = round(kilo * 0.6214, 2)

        tkinter.messagebox.showinfo(
            "Result", str(kilo + "kilometers is equal to " + str(miles) + "miles")
        )


kilo_conv = KiloConverterGUI()

print("moving on......")
