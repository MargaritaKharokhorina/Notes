import csv
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, askopenfiles, asksaveasfile
import os
#import pathlib
#from pathlib import Path


file_name = NONE


def new_file():
    global file_name
    file_name = "Без названия"
    text.delete('1.0', END)


def save_as():
    out = asksaveasfile(mode='w', defaultextension='csv')
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
    #text.delete('1.0', END)
    text.insert('1.0', data)

def delete_text():
    text.delete("1.0", END)
 


def list_files(event):
    content = os.listdir('/Users/kharo/OneDrive/Рабочий стол/Заметки')
    #content = askopenfiles(mode='r')
    print(content)
    



#def autosave():
    #way = "last_node.json"
    #text_save = text.get('1.0', END)
    #with open(way, "w", encoding='utf-8') as f:
        #json.dump(text_save, f, indent=4, ensure_ascii=False)
    #root.after(60000 * 1, autosave)

root = Tk()
root.title("Заметки")
root.geometry("400x400")
text = Text(root, width=400, height=400)

but1 = Button(root)
but1["text"] = "Просмотр списка заметок"
but1.bind("<Button-1>", list_files)

but2 = Button(root)
but2["text"] = "Удалить заметку"
but2.bind("<Button-2>", delete_text)

#button.pack()

but1.pack()
but2.pack()

text.pack()

notes_menu = Menu(root)
file_menu = Menu(notes_menu)
notes_menu.add_cascade(label="Работа с заметками", menu=file_menu)
file_menu.add_command(label="Создать новую заметку", command=new_file)
file_menu.add_command(label="Открыть заметку", command=open_file)
file_menu.add_command(label="Сохранить как", command=save_as)
#file_menu.add_command(label="Показать список заметок", command=list_files)







root.config(menu=notes_menu)

#way = 'last_node.json'
#with open(way) as f:
    #insert = json.load(f)
    #print(f"{insert}")
#text.insert(INSERT, insert)

root.mainloop()