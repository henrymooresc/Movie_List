import tkinter as tkr
from tkinter import ttk
import pandas as pd

def submit_fields():
    path = "movielist.xlsx"
    df1 = pd.read_excel(path)
    
    sTitle = df1["Title"]
    sDir = df1["Director"]
    #sGenre = df1["Genre(s)"]
    #sTheme = df1["Theme(s)"]
    #sRDate = df1["Release"]
    #sMPAA = df1["MPAA"]
    #sCast = df1["Cast"]
    #sRating = df1["Rating"]
    #sComment = df1["Comments"]
    
    title = pd.Series(eTitle.get())
    director = pd.Series(eDirector.get())

    sTitle = sTitle.append(title)
    sDir = sDir.append(director)

    df2 = pd.DataFrame({"Title":sTitle, "Director":sDir})
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