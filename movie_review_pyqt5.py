import sys
import pandas as pd
from PyQt5 import QtWidgets as qtw
#https://coderslegacy.com/python/pyqt5-tutorial/
#http://zetcode.com/gui/pyqt5/firstprograms/

comboData = {
    'genre': ['Action', 'Adventure', 'Comedy', 'Documentary', 'Drama', 'Horror', 'Musical', 'Romantic', 'Thriller'],
    'theme': ['Animated', 'Crime', 'Fantasy', 'Historical', 'Music', 'SciFi', 'War', 'Western']
    }

class MainWindow(qtw.QWidget):
    
    def __init__(self):
        super().__init__()
        self.UI()

    def submitForm(self):
        path = "movielist.xlsx"
        df1 = pd.read_excel(path)
        
        s_title = df1["Title"]
        #s_dir = df1["Director"]
        #s_genre = df1["Genre(s)"]
        #s_theme = df1["Theme(s)"]
        #s_rdate = df1["Release"]
        #s_mpaa = df1["MPAA"]
        #s_cast = df1["Cast"]
        #s_rating = df1["Rating"]
        #s_comment = df1["Comments"]

        title = pd.Series()
        s_title = s_title.append(title)

        df2 = pd.DataFrame({"Title":s_title})
        df2.to_excel(path, index=False)
        print("done?")


    def UI(self):
        title_line = qtw.QLineEdit()
        title_line.setPlaceholderText("Film Title")
        direct_line = qtw.QLineEdit()
        direct_line.setPlaceholderText("Director")
        date_line = qtw.QLineEdit()
        date_line.setPlaceholderText("Release Date (mm/dd/yyyy)")
        mpaa_line = qtw.QLineEdit()
        mpaa_line.setPlaceholderText("MPAA")
        cast_line = qtw.QLineEdit()
        cast_line.setPlaceholderText("Main Cast")
        comment_line = qtw.QLineEdit()
        comment_line.setPlaceholderText("Comments")

        quit_button = qtw.QPushButton()
        quit_button.setText("Quit")
        quit_button.clicked.connect(self.close)

        submit_button = qtw.QPushButton()
        submit_button.setText("Submit")
        submit_button.clicked.connect(self.submitForm())

        grid = qtw.QGridLayout()
        grid.addWidget(title_line, 0, 0)
        grid.addWidget(direct_line, 0, 1)
        grid.addWidget(date_line, 1, 0)
        grid.addWidget(mpaa_line, 1, 1)
        grid.addWidget(cast_line, 2, 0)
        grid.addWidget(comment_line, 2, 1)
        grid.addWidget(submit_button, 3, 0)
        grid.addWidget(quit_button, 3, 1)

        self.setLayout(grid)
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle("Movie Review Form")
        self.show()

def main():
    app = qtw.QApplication(sys.argv)
    gui = MainWindow()
    sys.exit(app.exec_())

main()
