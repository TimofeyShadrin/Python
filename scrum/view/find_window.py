from tkinter import *
from tkinter import ttk


def find_windows(event):
    find = Toplevel()
    find.title('Find employee')
    find.geometry('640x480')
    logo = PhotoImage(file="scrum.png")
    find.iconphoto(False, logo)
    find.grab_set()
    label = Label(find, text="\nPlease enter phrase in data of employee:\n")
    label.pack(anchor='w', padx=20)
    ttk.Entry(find).pack(anchor='w', padx=20)
