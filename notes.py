from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

#file_name = NONE

root = Tk()
root.title("Заметки")
root.geometry("400x400")

notes_menu = Menu(root)
file_menu = Menu(notes_menu)
notes_menu.add_cascade(label="Файл", menu=file_menu)

root.config(menu=notes_menu)
root.mainloop()