from tkinter import *


class Reg_Form(Frame):
    def __init__(self, master):
        super(Reg_Form, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        pass


window = Tk()
window.title("Registration Form")
window.geometry("300x300")

app = Reg_Form(window)
app.mainloop()