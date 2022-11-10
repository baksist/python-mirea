from tkinter import *

def get_center_offset(width, height):
    root = Tk()
    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
    root.destroy()
    left = (screen_width - width) // 2
    top = (screen_height - height) // 2
    return left, top

def init_form():

    def check_second_arg():
        return len(result_label["text"].split('+')) == 2
      
    def button_num1_click():
        if (check_second_arg()):
            button_eq.configure(state = "normal")
        result_label["text"] += "1"
    
    def button_num2_click():
        if (check_second_arg()):
            button_eq.configure(state = "normal")
        result_label["text"] += "2"
    
    def button_plus_click():
        result_label["text"] += "+"
        button_plus.configure(state = "disabled")
    
    def button_eq_click():
        args = result_label["text"].split('+')
        result_label["text"] += f"={int(args[0])+int(args[1])}"
        button_num1.configure(state = "disabled")
        button_num2.configure(state = "disabled")
        button_eq.configure(state = "disabled")
   
    def button_clear_click():
        result_label["text"] = ""
        button_num1.configure(state = "normal")
        button_num2.configure(state = "normal")
        button_plus.configure(state = "normal")
        button_eq.configure(state = "disabled")

    form = Tk()

    width, height = 640, 480
    left, top = get_center_offset(width, height)
    form_dimensions = f"{width}x{height}+{left}+{top}"
    app_title = "Simple Calculator"

    form.geometry(form_dimensions)
    form.title(app_title)

    button_num1 = Button(text = "1", command = button_num1_click)
    button_num2 = Button(text = "2", command = button_num2_click)
    button_plus = Button(text = "+", command = button_plus_click)
    button_eq = Button(text = "=", command = button_eq_click, state = "disabled")
    button_clear = Button(text = "Clear", command = button_clear_click)
    buttons = [button_num1, button_num2, button_plus, button_eq, button_clear]

    result_label = Label(text = "", font = ("Arial", 18))
    result_label.place(x = width // 6, y = height // 3)

    but_x, but_y = width // 6, 2 * (height // 3)
    
    for button in buttons:
        button.configure(font = ("Arial", 18))
        button.place(x = but_x, y = but_y)
        but_x += width // 8

    return form

if __name__ == "__main__":
    main_form = init_form()
    main_form.mainloop()