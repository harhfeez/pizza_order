from PyQt5 import Qtwidgets
from Ui_calculator import Ui_calculator
class Calculatorwindow(Qtwidgets.QMainwindow,Ui_calculator):
    def __init__(self):
        super().__init__()
        self.setupui(self)
        self.show()