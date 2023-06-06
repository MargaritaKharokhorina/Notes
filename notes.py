from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
from functions import *

file_name = NONE

def new_file():
    global file_name
    file_name = "Без названия"
    text.delete('1.0', END)


def save_as():
    out = asksaveasfile(mode='w', defaultextension='.json', encoding='utf-8')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("Нельзя сохранить файл")


def open_file():
    global file_name
    inp = askopenfile(mode='r')
    if inp is None:
        return 
    file_name = inp.name
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)



root = Tk()
root.title("Заметки")
root.geometry("400x400")
text = Text(root, width=400, height=400)
text.pack()

notes_menu = Menu(root)
file_menu = Menu(notes_menu)
file_menu.add_command(label="Новая заметка", command=new_file)
file_menu.add_command(label="Открыть заметку", command=open_file)
file_menu.add_command(label="Сохранить как", command=save_as)
notes_menu.add_cascade(label="Файл", menu=file_menu)




root.config(menu=notes_menu)
root.mainloop()