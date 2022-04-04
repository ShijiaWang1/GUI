from multiprocessing import Value
import tkinter

class PizzaGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # congifure the main window

        self.main_window.geometry("450x350")

        self.label1 = tkinter.Label(self.main_window, text="Hello! Welcome to the order menu.", font= ("Times",13,"bold"),foreground="orange", width=30,
    height=4)

        

        self.label1.pack(side="top")
        


        self.f1_frame = tkinter.Frame(self.main_window)
        self.f2_frame = tkinter.Frame(self.main_window)
        self.f3_frame = tkinter.Frame(self.main_window)
        self.f4_frame = tkinter.Frame(self.main_window)
        self.f5_frame = tkinter.Frame(self.main_window)

        self.prompt_label1 = tkinter.Label(
            self.f1_frame, text="Please tell us your name:",font= ("Times",10),width=30,height=2)
        self.test_entry1 = tkinter.Entry(self.f1_frame, width=15)

        self.prompt_label1.pack(side="left")
        self.test_entry1.pack(side="left")

        self.label2 = tkinter.Label(self.f2_frame, text="Please go ahead select your pizza",font= ("Times",10),width=30,height=2)
        self.label2.pack(side="top")


        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)

        self.cb1 = tkinter.Checkbutton(
            self.f3_frame, text="$3 Chicken", variable=self.cb_var1,
        )
        self.cb2 = tkinter.Checkbutton(
            self.f3_frame, text="$2 Pineapple", variable=self.cb_var2,
        )
        self.cb3 = tkinter.Checkbutton(
            self.f3_frame, text="$3 Ham", variable=self.cb_var3,
        )

        self.cb4 = tkinter.Checkbutton(
            self.f3_frame, text="$2 Extra cheese", variable=self.cb_var4,
        )

        self.cb1.pack(side="left")
        self.cb2.pack(side="left")
        self.cb3.pack(side="left")
        self.cb4.pack(side="left")

        self.mybutton = tkinter.Button(
            self.f5_frame, text="Calculate Cost",font=("Times", 8, "bold"),bg="green",width=12,height=4, command=self.pizza_cost
        )

        self.quit_button = tkinter.Button(
            self.f5_frame, text="Exit",font=("Times", 8, "bold"),bg="red",width=6,height=2, command=self.main_window.destroy
        )
        self.quit_button.pack(side="bottom")
        self.mybutton.pack(side="left")
        

        self.f1_frame.pack(side="top")
        self.f2_frame.pack(side="top")
        self.f3_frame.pack(side="top")
        self.f4_frame.pack(side="top")
        self.f5_frame.pack(side="top")

        self.crust_var = tkinter.IntVar()
        self.crust_var.set(8)

        self.rb1 = tkinter.Radiobutton(
            self.f4_frame, text="$8 Thin Crust", variable=self.crust_var, value=8
        )

        self.rb2 = tkinter.Radiobutton(
            self.f4_frame, text="$12 Thick Crust", variable=self.crust_var, value=12
        )

        self.rb3 = tkinter.Radiobutton(
            self.f4_frame, text="$14 Stuffed Crust", variable=self.crust_var, value=14
        )

        self.rb1.pack(side="left")
        self.rb2.pack(side="left")
        self.rb3.pack(side="left")



        tkinter.mainloop()


    def pizza_cost(self):
        total = (self.cb_var1.get()*3+ self.cb_var2.get()*2+self.cb_var3.get()*3+self.cb_var4.get()*2+self.crust_var.get())
    

        from tkinter import messagebox
        tkinter.messagebox.showinfo('Summary',self.test_entry1.get()+ " ,Your total cost: $" + str(total)
        )
        

        


my_gui = PizzaGUI()

print("moving on......")