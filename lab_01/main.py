from tkinter import *
from tkinter import ttk
from math import *

from matplotlib import mlab
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

from tkinter.messagebox import showerror, showwarning, showinfo

data_x = []
data_y = []
data = []

def check_points(x, y):
    try:
        x = float(x)
        y = float(y)
        return 1
    except ValueError:
        showerror(title = "Ошибка ввода", message = "Данные введены неверно")
        return 0

def add_points_graph():
    x = add_entry_x.get()
    y = add_entry_y.get()
    flag = check_points(x, y)
    if (flag):
        x = float(x)
        y = float(y)
        
        data_x.append(x)
        data_y.append(y)

        a = plt.plot(x, y, 'bo')
        data.append(a)

        plt.draw()



def del_points_graph():
    x = del_entry_x.get()
    y = del_entry_y.get()
    flag = check_points(x, y)

    if (flag):
        x = float(x)
        y = float(y)
        
        i = 0
        while i != len(data_x):
            if (data_x[i] == x and data_y[i] == y):
                break
            i += 1
        
        del data_x[i]
        del data_y[i]

        points = data[i][0]

        points.remove()

        plt.draw()

# def check_points(x, y):
#     try:
#         x = float(x)
#         y = float(y)
#         # if (0 > x or y < 0 or x > 100 or y > 100):
#             showerror(title = "Ошибка ввода", message = "Значение координат: 0 - 100")
#             return 0
#     except ValueError:
#         showerror(title = "Ошибка ввода", message = "Данные введены неверно")
#         return 0

#     return 1

def clear_graph():
    
    for i in range(len(data)):
        points = data[i][0]
        points.remove()

    plt.draw()

    data_x.clear()
    data_y.clear()
    data.clear()

def show_table_coords():
    root = Toplevel()
    root.title("METANIT.COM")
    root.geometry("250x300") 
    root.rowconfigure(index = 0, weight = 1)
    root.columnconfigure(index = 0, weight = 1)

    # определяем столбцы
    columns = ("x", "y")
    
    tree = ttk.Treeview(root, columns=columns, show = "headings")
    tree.grid(row = 0, column = 0, sticky = "nsew")
    
    # определяем заголовки
    tree.heading("x", text = "X", anchor = W)
    tree.heading("y", text = "Y", anchor = W)
    
    tree.column("#1", stretch = NO, width = 100)
    tree.column("#2", stretch = NO, width = 100)

    # добавляем данные
    for i in range(len(data_x)):
        tree.insert("", END, values = (data_x[i], data_y[i]))
    
    # добавляем вертикальную прокрутку
    scrollbar = ttk.Scrollbar(orient = VERTICAL, command = tree.yview)
    tree.configure(yscroll = scrollbar.set)
    scrollbar.grid(row = 0, column = 1, sticky = "ns")

def create_semi_perimeter(a, b, c):
    return (a + b + c) / 2

#поиск площади описанной окружности
def create_described_radius(a, b, c, p):
    return a * b * c / (4 * sqrt(p * (p - a) * (p - b) * (p - c)))


#поиск площади вписанной окружности
def create_inscribed_radius(a, b, c, p):
    return sqrt((p - a) * (p - b) * (p - c) / p)

#Поиск стороны треугольника
def create_side(x1, x2, y1, y2):
    return sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

#проверка сторон треугольника
def triangle_test(a, b, c):
    return a + b > c and b + c > a and c + a > b

#Поиск площади окружности
def create_sircle_square(r):
    return pi * pow(r, 2)

#Поиск треугольника
def search_triangle():
    if (len(data_x) < 3):
        showerror(title = "Ошибка", message = "Невозможно построить треугольник.\nТочек < 3")
    else:
        flag = 1
        res_indx = []
        minl = float("inf")
        for i in range(len(data_x)):
            for j in range(i + 1, len(data_x)):
                for k in range(j + 1, len(data_x)):
                    a = create_side(data_x[i], data_x[j], data_y[i], data_y[j])
                    b = create_side(data_x[i], data_x[k], data_y[i], data_y[k])
                    c = create_side(data_x[j], data_x[k], data_y[j], data_y[k])
                    if (triangle_test(a, b, c)):
                        p = create_semi_perimeter(a, b, c)
                        r_insc = create_inscribed_radius(a, b, c, p)
                        r_desc = create_described_radius(a, b, c, p)
                        s_insc = create_sircle_square(r_insc)
                        s_desc = create_sircle_square(r_desc)
                        if (minl > s_desc - s_insc):
                            minl = s_desc - s_insc
                            res_indx = [[data_x[i], data_x[j], data_x[k], data_x[i]], [data_y[i], data_y[j],  data_y[k], data_y[i]]]

                        flag = 0

        plt.plot(res_indx[0], res_indx[1], '-o', c = "red")
        plt.draw()
        

        if (flag):
            showerror(title = "Ошибка", message = "Треугольники не найдены")

                    

def application():
    window = Tk()
    window.title("Лабораторная 1")
    window.geometry("1100x800")

    #Построение вретикальной линии
    vertical_line = Frame(window, width = 5, height = 800, bg = "black")
    vertical_line.place(x = 800, y = 0)

    frame = Frame(window, width = 800, height = 800)
    frame.place(x = 0, y = 0)

    name_label = Label(window, text = "Управление", font = ("Arial", 30, "bold"))
    name_label.place(x = 860, y = 60)

    #Настройка графика
    global ax
    fig, ax = plt.subplots(dpi = 50, figsize = (8, 7.2), facecolor = "white")

    figure_canvas = FigureCanvasTkAgg(fig, frame)
    NavigationToolbar2Tk(figure_canvas, frame)

    figure_canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = 1)

    #Блок ввода координат точек для добавления
    add_label_x = Label(window, text = "X:", font = ("Arial", 25, "bold"))
    add_label_x.place(x = 810, y = 145)

    global add_entry_x
    add_entry_x = Entry(window, width = 10)
    add_entry_x.place(x = 840, y = 150)

    add_label_y = Label(window, text = "Y:", font = ("Arial", 25, "bold"))
    add_label_y.place(x = 950, y = 145)

    global add_entry_y
    add_entry_y = Entry(window, width = 10)
    add_entry_y.place(x = 980, y = 150)

    add_button = Button(window, text = "Добавить", font = ("Arial", 20, "bold"), command = add_points_graph)
    add_button.place(x = 890, y = 200)

    #Блок ввода координат точек для удаления
    del_label_x = Label(window, text = "X:", font = ("Arial", 25, "bold"))
    del_label_x.place(x = 810, y = 295)

    global del_entry_x
    del_entry_x = Entry(window, width = 10)
    del_entry_x.place(x = 840, y = 300)

    del_label_y = Label(window, text = "Y:", font = ("Arial", 25, "bold"))
    del_label_y.place(x = 950, y = 295)

    global del_entry_y
    del_entry_y = Entry(window, width = 10)
    del_entry_y.place(x = 980, y = 300)

    del_button = Button(window, text = "Удалить", font = ("Arial", 20, "bold"), command = del_points_graph)
    del_button.place(x = 890, y = 350)

    clear_button = Button(window, text = "Очистить", width = 15, height = 2, font = ("Arial", 20, "bold"), command = clear_graph)
    clear_button.place(x = 845, y = 410)

    show_button = Button(window, text = "Таблица", width = 15, height = 2, font = ("Arial", 20, "bold"), command = show_table_coords)
    show_button.place(x = 845, y = 470)

    start_button = Button(window, text = "Поиск", width = 15, height = 2, font = ("Arial", 20, "bold"), command = search_triangle)
    start_button.place(x = 845, y = 530)

    horizontal_line = Frame(window, width = 300, height = 5, bg = "black")
    horizontal_line.place(x = 800, y = 650)

    #Вывод правил пользования программой
    label_text_a = Label(window, text = "1)Ввод координат осуществляется с помощью \nцелых чисел или с чисел с плавающей точкой.",  font = ("Arial", 12))
    label_text_a.place(x = 805, y = 655)

    label_text_b = Label(window, text = "2)Вывод введенных координат отображается на \nграфике в виде точек и в таблице координат.",  font = ("Arial", 12))
    label_text_b.place(x = 805, y = 690)

    label_text_c = Label(window, text = "3)Для поиска треугольника нажмите кнопку 'Поиск'.",  font = ("Arial", 12))
    label_text_c.place(x = 805, y = 725)

    window.mainloop()


if __name__ == "__main__":
    application()


