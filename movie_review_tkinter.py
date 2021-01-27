import tkinter as tkr
from tkinter import ttk
import pandas as pd

def submit_fields():
    path = "movielist.xlsx"
    df1 = pd.read_excel(path)
    
    s_title = df1["Title"]
    s_dir = df1["Director"]
    s_genre = df1["Genre(s)"]
    s_theme = df1["Theme(s)"]
    s_rdate = df1["Release"]
    s_mpaa = df1["MPAA"]
    s_cast = df1["Cast"]
    s_rating = df1["Rating"]
    s_comment = df1["Comments"]
    
    title = pd.Series(eTitle.get())
    director = pd.Series(eDirector.get())

    s_title = s_title.append(title)
    s_dir = s_dir.append(director)

    df2 = pd.DataFrame({"Title":s_title, "Director":s_dir})
    df2.to_excel(path, index=False)

    eTitle.delete(0, tkr.END)
    eDirector.delete(0, tkr.END)


root = tkr.Tk()
root.geometry("500x500")
root.title("Film Rating Entry Form")

frame = tkr.Frame(root)
frame.pack()
topF = tkr.Frame(root)
topF.pack(side=tkr.TOP)
botF = tkr.Frame(root)
botF.pack(side=tkr.BOTTOM)
leftF = tkr.Frame(root)
leftF.pack(side=tkr.LEFT)
rightF = tkr.Frame(root)
rightF.pack(side=tkr.RIGHT)

eTitle = tkr.Entry(leftF, width=20)
eTitle.insert(0, "Film Title")
eTitle.pack(padx=3, pady=3)
eDirector = tkr.Entry(leftF, width=20)
eDirector.insert(0, "Director Name")
eDirector.pack(padx=3, pady=3)
eRelease = tkr.Entry(leftF, width=25)
eRelease.insert(0, "Release Date (mm/dd/yyyy)")
eRelease.pack(padx=3, pady=3)

#tkr.Button(root, text="Quit", command=root.quit).grid(row=5, column=0, pady=4)
#tkr.Button(root, text="Submit", command=submit_fields).grid(row=5, column=1, pady=4)

tkr.mainloop()