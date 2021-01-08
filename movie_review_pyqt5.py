import sys
import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLineEdit, QApplication, QMenu, QWidget, QComboBox, QDateEdit, QToolButton, QPushButton, QGridLayout)

#https://doc.qt.io/qt-5/index.html

list_choices = {
    "genre": ["Action", "Adventure", "Comedy", "Documentary", "Drama", "Horror", "Musical", "Romantic", "Thriller"],
    "theme": ["Animated", "Crime", "Fantasy", "Historical", "Music", "SciFi", "War", "Western"],
    "mpaa": ["G", "PG", "PG-13", "R"]
    }

class FilmReviewForm(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.title_line = QLineEdit()
        self.title_line.setPlaceholderText("Film Title")
        self.direct_line = QLineEdit()
        self.direct_line.setPlaceholderText("Director")
        self.cast_line = QLineEdit()
        self.cast_line.setPlaceholderText("Main Cast")
        self.rating_line = QLineEdit()
        self.rating_line.setPlaceholderText("Rating /10")
        self.comment_line = QLineEdit()
        self.comment_line.setPlaceholderText("Comments")

        self.mpaa_cb = QComboBox(self)
        self.mpaa_cb.addItems(list_choices["mpaa"])

        self.date_cal = QDateEdit(self)
        self.date_cal.setCalendarPopup(True)

        self.genre_tb = QToolButton(self)
        self.genre_tb.setText("Select Genre(s)")
        self.genre_tm = QMenu(self)
        for g in list_choices["genre"]:
            action = self.genre_tm.addAction(g)
            action.setCheckable(True)
        self.genre_tb.setMenu(self.genre_tm)
        self.genre_tb.setPopupMode(QToolButton.InstantPopup)

        self.theme_tb = QToolButton(self)
        self.theme_tb.setText("Select Theme(s)")
        self.theme_tm = QMenu(self)
        for g in list_choices["theme"]:
            action = self.theme_tm.addAction(g)
            action.setCheckable(True)
        self.theme_tb.setMenu(self.theme_tm)
        self.theme_tb.setPopupMode(QToolButton.InstantPopup)

        quit_button = QPushButton()
        quit_button.setText("Quit")
        quit_button.clicked.connect(self.close)

        submit_button = QPushButton()
        submit_button.setText("Submit")
        submit_button.clicked.connect(self.submitForm)

        grid = QGridLayout()
        grid.addWidget(self.title_line, 0, 0)
        grid.addWidget(self.direct_line, 0, 1)
        grid.addWidget(self.genre_tb, 0, 2)
        grid.addWidget(self.theme_tb, 1, 2)
        grid.addWidget(self.date_cal, 1, 0)
        grid.addWidget(self.mpaa_cb, 1, 1)
        grid.addWidget(self.cast_line, 2, 0)
        grid.addWidget(self.rating_line, 2, 1)
        grid.addWidget(self.comment_line, 2, 2)
        grid.addWidget(submit_button, 3, 0)
        grid.addWidget(quit_button, 3, 2)

        self.setLayout(grid)
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle("Movie Review Form")
        self.show()

    def submitForm(self):
        path = "movielist.xlsx"
        df1 = pd.read_excel(path)
        
        s_title = df1["Title"]
        s_dir = df1["Director"]
        s_genre = df1["Genre(s)"]
        s_theme = df1["Theme(s)"]
        s_rdate = df1["Release Date"]
        s_mpaa = df1["MPAA"]
        s_cast = df1["Cast"]
        s_rating = df1["Rating"]
        s_comment = df1["Comments"]
        
        title = pd.Series(self.title_line.text())
        director = pd.Series(self.direct_line.text())
        cast = pd.Series(self.cast_line.text())
        rating = pd.Series(self.rating_line.text())
        comment = pd.Series(self.comment_line.text())

        mpaa = pd.Series(self.mpaa_cb.currentText())
        
        rdate = pd.Series(self.date_cal.dateTime().toString("MM/dd/yyyy"))

        c_genres = []
        for g in self.genre_tm.actions():
            if g.isChecked():
                c_genres.append(g.text())
        genres = pd.Series(", ".join(c_genres))

        c_themes = []
        for t in self.theme_tm.actions():
            if t.isChecked():
                c_themes.append(t.text())
        themes = pd.Series(", ".join(c_themes))

        s_title = s_title.append(title)
        s_dir = s_dir.append(director)
        s_genre = s_genre.append(genres)
        s_theme = s_theme.append(themes)
        s_rdate = s_rdate.append(rdate)
        s_mpaa = s_mpaa.append(mpaa)
        s_cast = s_cast.append(cast)
        s_rating = s_rating.append(rating)
        s_comment = s_comment.append(comment)

        df2 = pd.DataFrame({"Title": s_title, "Director": s_dir, "Genre(s)": s_genre, "Theme(s)": s_theme, "Release Date": s_rdate, "MPAA": s_mpaa, "Cast": s_cast, "Rating": s_rating, "Comments": s_comment})
        df2.to_excel(path, index=False)
        print("Submitted...")

        self.title_line.clear()
        self.direct_line.clear()
        self.cast_line.clear()
        self.rating_line.clear()
        self.comment_line.clear()
        
        for g in self.genre_tm.actions():
            if g.isChecked():
                g.setChecked(False)

        for t in self.theme_tm.actions():
            if t.isChecked():
                t.setChecked(False)

def main():
    app = QApplication(sys.argv)
    gui = FilmReviewForm()
    sys.exit(app.exec_())

main()
