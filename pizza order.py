from tkinter import *

class Form(Frame):

    def __init__(self, master):
        super(Form, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.toppings = ["Sausage", "Pepperoni", "Chicken", "Mushroom", "Black Olive", "Green Pepper", "Red Pepper", "Onion"]
        self.prices = {"medium": 2500, "large": 3500, "xlarge": 5000, "m_topping": 100, "l_topping": 150, "x_topping": 200}
        self.lbl_title = Label(self, text="Python Pizza Calculator")
        self.lbl_title.grid(row=0, column=0, columnspan=2, sticky=E)
        self.lbl_empty = Label(self, text="").grid(row=1, column=0)

        self.size = StringVar()
        self.lbl_ss = Label(self, text="Select Size: ")
        self.lbl_ss.grid(row=2, column=0, sticky=W)
        self.rad_medium = Radiobutton(self, text="Medium", value="Medium", variable=self.size)
        self.rad_medium.grid(row=3, column=0, sticky=W)
        self.rad_large = Radiobutton(self, text="Large", value="Large", variable=self.size)
        self.rad_large.grid(row=3, column=1, sticky=W)
        self.rad_xlarge = Radiobutton(self, text="Extra Large", value="x-Large", variable=self.size)
        self.rad_xlarge.grid(row=3, column=2, sticky=W)
        self.rad_medium.select()
        self.lbl_empty = Label(self, text="").grid(row=4, column=0)

        self.lbl_st = Label(self, text="Select Toppings: ")
        self.lbl_st.grid(row=5, column=0, sticky=W)
        self.chkVar = list(self.toppings)
        self.chk = list(self.toppings)

        line = 6

        for i in range(len(self.toppings)):
            self.chkVar[i] = BooleanVar()
            self.chk[i] = Checkbutton(self, text=self.toppings[i], variable=self.chkVar[i])
            self.chk[i].grid(row=line, column=1, sticky=W)
            line += 1

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0)

        line += 1
        self.btn_reset = Button(self, text="Reset", width=10, command=self.reset)
        self.btn_reset.grid(row=line, column=0, sticky=E)
        self.btn_submit = Button(self, text="Submit Order", command=self.calculate)
        self.btn_submit.grid(row=line, column=1, sticky=W)

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0)

        line += 1
        self.lbl_total = Label(self, text="Total: ").grid(row=line, column=0, sticky=E)
        self.total = Entry(self, text="", width=10)
        self.total.grid(row=line, column=1, sticky=W)

        self.err = StringVar()
        self.lbl_feedback = Label(self, text="", foreground='red', textvariable=self.err).grid(row=line, column=2, sticky=W)

    def reset(self):
        self.rad_medium.select()

        for i in range(len(self.toppings)):
            self.chk[i].deselect()

        self.total.delete(0, END)


    def calculate(self):
        self.total.delete(0, END)
        total_price = 0
        total_toppings = 0
        selected_toppings = []

        for i in range(len(self.toppings)):
            if self.chkVar[i].get():
                total_toppings += 1
                selected_toppings.append(self.chk[i]['text'] )

        if total_toppings == 0:
            total_price = 0
            self.err.set("please select at \nleast one topping")
        else:
            if self.size.get() == "Medium":
                total_price = self.prices['medium'] + (self.prices['m_topping'] * total_toppings)
                order = 'Pizza Size: {} \t {}'.format(self.size.get(), self.prices['medium'])
                order += '\nToppings: '
                for i in range(len(selected_toppings)):
                    order += '{} \t {}\n\t\t'.format(selected_toppings[i], self.prices['m_topping'])
            elif self.size.get() == "Large":
                total_price = self.prices['large'] + (self.prices['l_topping'] * total_toppings)
                order = 'Pizza Size: {} \t {}'.format(self.size.get(), self.prices['large'])
                order += '\nToppings: '
                for i in range(len(selected_toppings)):
                    order += '{} \t {}\n\t\t'.format(selected_toppings[i], self.prices['l_topping'])
            elif self.size.get() == "x-Large":
                total_price = self.prices['xlarge'] + (self.prices['x_topping'] * total_toppings)
                order = 'Pizza Size: {} \t {}'.format(self.size.get(), self.prices['xlarge'])
                order += '\nToppings: '
                for i in range(len(selected_toppings)):
                    order += '{} \t {}\n\t\t'.format(selected_toppings[i], self.prices['x_topping'])

            order += '\nTotal: {}'.format(total_price)
            order += '\n\n'
            msg = "order valued =N={}  \nsuccessfully submitted...".format(total_price)
            self.err.set(msg)

            self.total.insert(END, total_price)
            with open('order.txt', 'a') as file:
                file.write(order)
                file.close()
            self.reset()





window = Tk()
window.title("Python Pizza App")
window.geometry('350x450')
app = Form(window)
app.mainloop()