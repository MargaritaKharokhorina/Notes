from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
from functions import *

#file_name = NONE

root = Tk()
root.title("Заметки")
root.geometry("400x400")
text = Text(root, width=400, height=400)
text.pack()

notes_menu = Menu(root)
file_menu = Menu(notes_menu)
file_menu.add_command(label="Новая заметка", command=new_file)
notes_menu.add_cascade(label="Файл", menu=file_menu)


root.config(menu=notes_menu)
root.mainloop()