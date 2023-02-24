from tkinter import Tk
import classes

# from matplotlib import mlab
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import (
#     FigureCanvasTkAgg,
#     NavigationToolbar2Tk
# )
        

if __name__ == "__main__":
    window = Tk()
    classes.MainWindow(window)
    window.mainloop()