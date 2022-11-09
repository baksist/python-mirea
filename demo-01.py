from tkinter import *


def click_1():
    label_1["text"] = "test 2"


form_1 = Tk()

# width, height = 800, 600
# left, top = (form_1.winfo_screenwidth() - width) // 2,\
#             (form_1.winfo_screenheight() - height) // 2

width, height = form_1.winfo_screenwidth(), form_1.winfo_screenheight()
left, top = 0, 0

form_params = f"{width}x{height}+{left}+{top}"
form_1.geometry(form_params)
form_1.title("demo-app")

form_1.configure(background='pale green')

label_1 = Label(text="test", fg="red", bg="yellow")
label_1.place(x=5, y=5)

# button_1 = Button(text="click", command=click_1)
# button_1.place(x=5, y=30)
Button(text="click", command=click_1, bg="#FF0000").place(x=5, y=40)

form_1.mainloop()
