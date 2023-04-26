import sys
from PyQt5.Qtwidgets import QApplication
from calculate import Calculatorwindow

app = QApplication(sys.argv)
calculate = Calculatorwindow()

sys.exit(app.exec_())