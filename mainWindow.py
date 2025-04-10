from tkinter import Tk, Frame

from displayFrame import DisplayFrame
from navFrame import NavFrame


class MainWindow(Tk):
    HEIGHT = 500
    WIDTH = 1000

    def __init__(self):
        super().__init__()
        x = round(self.winfo_screenwidth() / 2 - self.WIDTH / 2)
        y = round(self.winfo_screenheight() / 2 - self.HEIGHT / 2)
        self.title("Калькулятор финансов")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}+{x}+{y}")
        # Настройка весов разметочной сетки
        # Единственная строка занимает все пространство
        self.grid_rowconfigure(0, weight=1)
        # Первый столбец - 1/4 часть пространства
        self.grid_columnconfigure(0, weight=1)
        # Второй столбец - 3/4 части пространства
        self.grid_columnconfigure(1, weight=3)

        nav_frame = NavFrame(self)
        nav_frame.grid(column=0, row=0, sticky="nsew")

        main_frame = DisplayFrame(self)
        main_frame.grid(column=1, row=0, sticky="nsew")

    def run(self):
        self.mainloop()
