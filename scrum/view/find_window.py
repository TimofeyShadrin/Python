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

    my_entry = ttk.Entry(find)
    my_entry.pack(anchor='w', padx=20)

    def receive_click():
        incoming = my_entry.get()
        return incoming

    receive = ttk.Button(find, text='Find', command=print(receive_click()))
    receive.pack(anchor='center')

    to_main = ttk.Button(find, text='Close')
    to_main.pack(anchor='center')
    to_main.bind('<ButtonPress-1>', lambda x=event: find.destroy())
