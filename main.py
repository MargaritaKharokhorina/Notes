#Напишите проект, содержащий функционал работы с заметками. 
#Программа должна уметь создавать заметку, сохранять ее, 
#читать список заметок, редактировать заметку, удалять заметку.


#Данная программа предполагает централизованную папку на вашем компьютере, в которой хранятся все заметки.



from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
import os


file_name = NONE


def new_file():
    global file_name
    file_name = "Untitled"
    text.delete('1.0', END)


def save_as(): # эта фун-ция также отвечает за редактирование, поскольку внеся изменения в файл, мы можем пересохранить его в имеющийся
    out = asksaveasfile(mode='w', defaultextension='csv')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("Can't save file")



def open_file():
    global file_name
    inp = askopenfile(mode='r')
    if inp is None:
        return 
    file_name = inp.name
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)


def list_remove_files(event):  # вывод в консоль
    content = os.listdir('Files')
    print("Your list of notes: ")
    print(content)
    path = input("Copy and paste the relative path of the file you want to delete: ")
    try:
        os.remove(path)
        print("File removed successfully")
    except FileNotFoundError:
        print("Invalid file path, try again")

def sort_by_date(event1): # вывод в консоль
    path = "Files"
    file_list = os.listdir(path)
    full_list = [os.path.join(path, i) for i in file_list]
    time_sorted_list = sorted(full_list, key = os.path.getmtime)
    print("Sort notes by date:")
    print(time_sorted_list)




root = Tk()
root.title("Notes")
root.geometry("400x400")
text = Text(root, width=400, height=400)

# кнопка "Просмотр списка заметок и удаление"
but1 = Button(root)
but1["text"] = "Viewing the list of notes and deleting"
but1.bind("<Button-1>", list_remove_files)
# кнопка "Сортировка по дате"
but2 = Button(root)
but2["text"] = "Sort by date: from early to late"
but2.bind("<Button-1>", sort_by_date)

but1.pack()
but2.pack()
text.pack()

notes_menu = Menu(root)
file_menu = Menu(notes_menu)
notes_menu.add_cascade(label="Working with notes", menu=file_menu)
file_menu.add_command(label="Create a new note", command=new_file)
file_menu.add_command(label="Open note", command=open_file)
file_menu.add_command(label="Save as", command=save_as)


root.config(menu=notes_menu)

root.mainloop()