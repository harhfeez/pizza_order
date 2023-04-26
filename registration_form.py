from tkinter import *

class Reg_Form(Frame):
    def __init__(self, master):
        super(Reg_Form, self).__init__(master)
        self.grid()
        self.create_widgets()



    def create_widgets(self):

        self.lbl_lname = Label(self, text= "Lastname: ")
        self.lbl_lname.grid(row=3, column=0, sticky=W)
        self.txt_lname = Entry(self, width=30)
        self.txt_lname.grid(row=3, column=1, columnspan=2, sticky=W)

        self.lbl_fname = Label(self, text="Firstname: ")
        self.lbl_fname.grid(row=4, column=0, sticky=W)
        self.txt_fname = Entry(self, width=30)
        self.txt_fname.grid(row=4, column=1, columnspan=2, sticky=W)

        self.lbl_uname = Label(self, text="Username: ")
        self.lbl_uname.grid(row=5, column=0, sticky=W)
        self.txt_uname = Entry(self, width=30)
        self.txt_uname.grid(row=5, column=1, columnspan=2, sticky=W)

        self.lbl_pword = Label(self, text="Password: ")
        self.lbl_pword.grid(row=6, column=0, sticky=W, )
        self.txt_pword = Entry(self, width=30, show="*")
        self.txt_pword.grid(row=6, column=1, columnspan=2, sticky=W)

        self.gender = StringVar()
        self.lbl_gender = Label(self, text="Gender: ")
        self.lbl_gender.grid(row=7, column=0, sticky=W)
        self.rad_male = Radiobutton(self, text="Male", value="Male", variable=self.gender)
        self.rad_male.grid(row=7, column=1, sticky=W)
        self.rad_female = Radiobutton(self, text="Female", value="Female", variable=self.gender)
        self.rad_female.grid(row=7, column=2, sticky=W)
        self.rad_male.select()

        self.marital_status = StringVar()
        self.marital_status_values = ['single', 'Married','Divorced', 'Single N Searching', 'Complicated']
        self.lbl_marital_status = Label(self, text="Marital status: ")
        self.lbl_marital_status.grid(row=8, column=0, sticky=W)
        self.option_marital_status = OptionMenu(self, self.marital_status, *self.marital_status_values)
        self.option_marital_status.grid(row=8, column=1, columnspan=2, sticky=W)
        self.marital_status.set(self.marital_status_values[0])


        line = 9
        self.lbl_hobbies = Label(self, text="Hobbies: ")
        self.lbl_hobbies.grid(row=9, column=0, columnspan=2, sticky=W)
        self.hobbies = ["Singing", "Dancing", "Movies", "flexing"]
        self.chkVar = list(self.hobbies)
        self.chk = list(self.hobbies)

        for i in range(len(self.hobbies)):
            self.chkVar[i] = BooleanVar()
            self.chk[i] = Checkbutton(self, text=self.hobbies[i], variable=self.chkVar[i])
            self.chk[i].grid(row=line, column=1, columnspan=2, sticky=W)
            line += 1

        line += 1
        self.lbl_ps = Label(self, text="Personal statement: ")
        self.lbl_ps.grid(row=line, column=0, sticky=W)
        self.txt_ps = Text(self, width=25, height=5)
        self.txt_ps.grid(row=line, column=1, columnspan=2, sticky=W)
        self.yscrollbar = Scrollbar(self, command=self.txt_ps.yview)
        self.yscrollbar.grid(row=line, column=3, sticky='nsew')
        self.txt_ps['yscrollcommand'] = self.yscrollbar.set

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0)

        line += 1
        self.btn_reset = Button(self, text="Reset", width=10, command=self.reset)
        self.btn_reset.grid(row=line, column=0, sticky=E)
        self.btn_submit = Button(self, text="Submit", width=10,command=self.submit)
        self.btn_submit.grid(row=line, column=1, sticky=W)


    def reset(self):
        self.txt_lname.delete(0, END)
        self.txt_fname.delete(0, END)
        self.txt_uname.delete(0, END)
        self.txt_pword.delete(0, END)
        self.rad_male.select()
        self.marital_status.set(self.marital_status_values[0])
        self.txt_ps.delete(0.0, END)

        for i in range(len(self.hobbies)):
            self.chk[i].deselect()

            self.txt_ps.delete(0.0, END)

    def submit(self):
        data = 'Lastname: ' +self.txt_lname.get()
        data += '\nFirstname: ' +self.txt_fname.get()
        data += '\nUsername: ' +self.txt_uname.get()
        data += '\nPassword: ' +self.txt_pword.get()
        data += '\nGender: ' +self.gender.get()
        data += '\nMarital status: ' +self.marital_status.get()
        data += '\nHobbies: '

        for i in range(len(self.hobbies)):
            if self.chkVar[i].get():
                data += self.chk[i]['text'] + ' '

        data += '\nPersonal statement: ' + self.txt_ps.get(1.0, END)
        data +='\n\n'
        print(data)
        with open('regform.txt', 'a') as f:
            f.write(data)
            f.close()
        self.reset()







window = Tk()
window.title("Registration Form")
window.geometry("400x400")


app = Reg_Form(window)
app.mainloop()