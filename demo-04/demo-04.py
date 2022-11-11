from tkinter import *
import constants as CN

def menu_save(event = None):
    s = text_1.get(1.0, END)
    with open(CN.FILENAME + CN.EXTENSION, 'w', encoding = 'utf-8') as file:
        file.write(s)


def menu_fill(event = None):
    text_1.insert("1.0", CN.SAMPLE_TEXT)

def menu_exit(event = None):
    exit(0)

form_1 = Tk()

width, height = 500, 200
left = (form_1.winfo_screenwidth() - width) // 2
top = (form_1.winfo_screenheight() - height) // 2

form_dims = f"{width}x{height}+{left}+{top}"
form_1.geometry(form_dims)

main_menu = Menu()

menu_1 = Menu(main_menu, tearoff = 0)
main_menu.add_cascade(label = "File", menu = menu_1)
form_1.config(menu = main_menu)

menu_1.add_cascade(label = "Open")
menu_1.add_command(label = "Save", command = menu_save, accelerator = "Ctrl+S")
menu_1.add_separator()
menu_1.add_command(label = "Exit", command = menu_exit, accelerator = "Ctrl+E")

text_1 = Text()
text_1.pack(expand = True, fill = "both")

form_1.bind("<Control-e>", menu_exit)
form_1.bind("<Control-f>", menu_fill)
form_1.bind("<Control-s>", menu_save)

form_1.mainloop()