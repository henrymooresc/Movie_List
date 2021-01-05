import sys
from PyQt5 import QtWidgets as qtw
#https://coderslegacy.com/python/pyqt5-tutorial/

class Layout(qtw.QWidget):
    
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        titleLine = qtw.QLineEdit("Film Title")

        subButton = qtw.QPushButton("Submit")

        grid = qtw.QGridLayout()
        grid.addWidget(titleLine, 0, 0)
        grid.addWidget(subButton, 1, 1)

        self.setLayout(grid)
        self.setGeometry(400, 400, 300, 300)
        self.setWindowTitle("Movie Review Form")
        self.show()

def main():
    app = qtw.QApplication(sys.argv)
    ex = Layout()
    sys.exit(app.exec_())

main()