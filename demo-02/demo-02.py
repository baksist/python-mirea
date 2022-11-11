from tkinter import *

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
menu_1.add_cascade(label = "Save")
menu_1.add_separator()
menu_1.add_cascade(label = "Exit", command = menu_exit, accelerator = "Ctrl+E")

form_1.bind("<Control-e>", menu_exit)

form_1.mainloop()