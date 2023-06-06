
file_name = None

def new_file():
    global file_name
    file_name = "Без названия"
    text.delete('1.0', END)


def save_as():
    out = asksaveasfile(mode='w', defaltextension='.txt')
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