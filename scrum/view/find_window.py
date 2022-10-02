from tkinter import *
from tkinter import ttk
from scrum.find import find_worker as fw

result = ''
count = 0


def find_windows(event):
    find = Toplevel()
    find.title('Find employee')
    find.geometry('720x640')
    logo = PhotoImage(file="scrum.png")
    find.iconphoto(False, logo)
    find.grab_set()
    label = Label(find, text="\nPlease enter phrase in data of employee:\n")
    label.pack(anchor='w', padx=20)

    my_entry = ttk.Entry(find)
    my_entry.pack(anchor='w', padx=20, fill=X)

    def receive_click():
        global result
        global count
        if count == 0:
            incoming = my_entry.get()
            result = str(incoming)
            fw.find_worker(result)

            languages_var = Variable(value=fw.all_list)
            languages_listbox = Listbox(find, listvariable=languages_var)
            languages_listbox.pack(anchor='center', fill=BOTH, padx=20, pady=20)

            scrollbar = ttk.Scrollbar(find, orient='horizontal', command=languages_listbox.xview)
            scrollbar.pack(after=languages_listbox, fill=X, padx=20)
            languages_listbox["xscrollcommand"] = scrollbar.set

            fw.all_list.clear()
            count += 1

    receive = ttk.Button(find, text='Find')
    receive.pack(anchor='se', padx=20, pady=20)
    receive.bind('<ButtonPress-1>', lambda x=event: receive_click())

    to_main = ttk.Button(find, text='Close')
    to_main.pack(anchor='se', padx=20)
    to_main.bind('<ButtonPress-1>', lambda x=event: find.destroy())
