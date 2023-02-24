from tkinter import Frame, TOP, BOTH, Label, Entry, Button
from matplotlib import mlab
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
import picture

class MainWindow:
    def __init__(self, master):
        self.master = master

        #Основные настройки окна
        master.title("Лабораторная 2")
        master.geometry("1300x800")

        #Настройки окна меню
        frame_menu = Frame(master, width = 400, height = 800, bg = "gray")
        FrameMenu(frame_menu)
        frame_menu.place(x = 0, y = 0)

        #Горизонтальная линия
        frame_line = Frame(master, width = 5, height = 800, bg = "black")
        frame_line.place(x = 395, y = 0)

        #Окно-граф
        # graph_frame = Frame(master, width = 900, height = 800)
        # graph_frame.place(x = 400, y = 0)

        # figure = plt.Figure(figsize=(8.5, 7.5))
        # figure.subplots_adjust()
        # subplt = figure.add_subplot(111)

        # figure_canvas = FigureCanvasTkAgg(fig, graph_frame)
        # NavigationToolbar2Tk(figure_canvas, graph_frame)

        margins = {
            "left"   : 0.050,
            "bottom" : 0.050,
            "right"  : 0.980,
            "top"    : 0.980
        }

        graph = picture.create_picture()

        figure = plt.Figure(figsize=(8.5, 7.5))
        figure.subplots_adjust(**margins)
        subplt = figure.add_subplot(111)

        for func in graph:
            subplt.plot(func[0], func[1], color='k', linewidth=2)

        subplt.set_xlim((-80, 80))
        subplt.set_ylim((-80, 80))
        subplt.grid(True)


        pltcnv = FigureCanvasTkAgg(figure, master)
        pltcnv.get_tk_widget().place(
            relx = 0.309,
            rely = 0.00,
            relheight = 1,
            relwidth = 0.69
            )
        
        # for i in graph:
        #     plt.plot(i[0], i[1])


        # figure_canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = 1)

        

class FrameMenu:
    def __init__(self, master):
        center_picture = Label(master, text = "X:{:7.2f}; Y:{:7.2f}".format(0, 0), width = 30, height = 2)
        center_picture.place(x = 55, y = 40)


class ConvertFrame:
    def __init__(self, master, name, a, b, c, operation):
        pass


# lbl_figure_centre.configure(
#             font=update.FONT_CONFIG,
#             text="X:{:7.2f}; Y:{:7.2f}".format(funcs[0].x_list[0],
#                                                funcs[0].y_list[0])
#             )