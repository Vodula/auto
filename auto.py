from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.title("Вибір автомобіля")

make_label = Label(root, text="Марка").place(x=20, y=10)

make_var = IntVar()
m1 = Radiobutton(root, text='BMW', variable=make_var, value=1).place(x=20, y=30)
m2 = Radiobutton(root, text='Mercedes', variable=make_var, value=2).place(x=20, y=50)
m3 = Radiobutton(root, text='Toyota', variable=make_var, value=3).place(x=20, y=70)

engine_label = Label(root, text="Об'єм двигуна").place(x=200, y=10)

engine = IntVar()
e1 = Radiobutton(root, text="1-2 літри", variable=engine, value=1).place(x=200, y=30)
e2 = Radiobutton(root, text="3 літри", variable=engine, value=2).place(x=200, y=50)
e3 = Radiobutton(root, text="більше 3 літрів", variable=engine, value=3).place(x=200, y=70)

year_label = Label(root, text="Рік").place(x=400, y=10)

vid = IntVar()
v1 = Radiobutton(root, text='до 5 років', variable=vid, value=1).place(x=400, y=30)
v2 = Radiobutton(root, text='до 10 років', variable=vid, value=2).place(x=400, y=50)
v3 = Radiobutton(root, text='від 10 років', variable=vid, value=3).place(x=400, y=70)


def choose_color():
    color = colorchooser.askcolor(title="Вибрати колір")
    if color[1]:
        print("Вибраний колір:", color[1])


color_button = Button(root, text="Вибрати колір", command=choose_color)
color_button.place(x=400, y=110)


def save_data():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, 'w') as file:
            file.write("Марка: ")
            if make_var.get() == 1:
                file.write("BMW\n")
            elif make_var.get() == 2:
                file.write("Mercedes\n")
            elif make_var.get() == 3:
                file.write("Toyota\n")
            file.write("Об'єм двигуна: ")
            if engine.get() == 1:
                file.write("1-2 літри\n")
            elif engine.get() == 2:
                file.write("3 літри\n")
            elif engine.get() == 3:
                file.write("більше 3 літрів\n")
            file.write("Рік: ")
            if vid.get() == 1:
                file.write("до 5 років\n")
            elif vid.get() == 2:
                file.write("до 10 років\n")
            elif vid.get() == 3:
                file.write("від 10 років\n")
            messagebox.showinfo('Дані', 'Дані успішно збереженні')


save_button = Button(root, text="Результат вибору", command=save_data)
save_button.place(x=400, y=140)

root.mainloop()
