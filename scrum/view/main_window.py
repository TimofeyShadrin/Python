from tkinter import *
from tkinter import ttk
import find_window as fw

root = Tk()  # создаем корневой объект - окно

root.title("Scrum-команда")  # устанавливаем заголовок окна
root.geometry("300x250")  # устанавливаем размеры окна
icon = PhotoImage(file="scrum.png")
root.iconphoto(False, icon)

label = Label(text="\nMain menu:\n")  # создаем текстовую метку
label.pack()  # размещаем метку в окне

find = ttk.Button(text="Find employee")
find.pack(fill=X)
find.bind('<ButtonPress-1>', fw.find_windows)

create = ttk.Button(text="Create record")  # создаем кнопку из пакета ttk
create.pack(fill=X)  # размещаем кнопку в окне



def destroy(event):
    root.destroy()


close = ttk.Button(text="Exit")
close.pack(fill=X)
close.bind("<ButtonPress-1>", destroy)

root.mainloop()
