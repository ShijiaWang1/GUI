from cgitb import text
import tkinter
from turtle import left, width



class ExerciseGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("500x200")

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.bottom_frame2 = tkinter.Frame(self.main_window)
        self.bottom_frame3 = tkinter.Frame(self.main_window)

        self.prompt_label1 = tkinter.Label(
            self.top_frame, text="Enter a score for test 1:"
        )
        self.prompt_label2 = tkinter.Label(
            self.mid_frame, text="Enter a score for test 2:"
        )
        self.prompt_label3 = tkinter.Label(
            self.bottom_frame, text="Enter a score for test 3:"
        )
        self.label4 = tkinter.Label(self.bottom_frame2, text="Average:")

        self.test_entry1 = tkinter.Entry(self.top_frame, width=10)
        self.test_entry2 = tkinter.Entry(self.mid_frame, width=10)
        self.test_entry3 = tkinter.Entry(self.bottom_frame, width=10)

        self.prompt_label1.pack(side="left")
        self.test_entry1.pack(side="left")
        self.prompt_label2.pack(side="left")
        self.test_entry2.pack(side="left")
        self.prompt_label3.pack(side="left")
        self.test_entry3.pack(side="left")
        self.label4.pack(side="left")

        self.top_frame.pack(side="top")
        self.mid_frame.pack(side="top")
        self.bottom_frame.pack(side="top")
        self.bottom_frame2.pack(side="top")
        self.bottom_frame3.pack(side="top")

        self.calcbutton = tkinter.Button(
            self.bottom_frame3, text="Average", command=self.average
        )

        self.quit_button = tkinter.Button(
            self.bottom_frame3, text="Quit", command=self.main_window.destroy
        )

        self.calcbutton.pack(side="left")
        self.quit_button.pack(side="right")

        tkinter.mainloop()

    def average(self):
        averagescore = (
            float(self.test_entry1.get())
            + float(self.test_entry2.get())
            + float(self.test_entry3.get())
        )

        finalscore = float(averagescore / 3)

        tkinter.messagebox.showinfo("Result", finalscore)


my_gui = ExerciseGUI()

print("moving on......")
