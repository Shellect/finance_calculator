from sqlite3 import adapt
from tkinter import Frame, Button, Toplevel, Label, Entry, StringVar
from tkinter.ttk import Radiobutton, Combobox
from tkinter.constants import RAISED


class NavFrame(Frame):
    is_modal_opened = False

    def __init__(self, root):
        super().__init__(root)
        self.add_window = None
        self.config(bg="white", bd=2, relief="groove")

        add_transaction_btn = Button(self, text="Добавить транзакцию", width=30, relief=RAISED,
                                     command=self.open_transaction_window)
        add_transaction_btn.pack(side="top", pady=15, anchor="center")

        get_transactions_btn = Button(self, text="Посмотреть транзакции", width=30, relief=RAISED)
        get_transactions_btn.pack(side="top", pady=15, anchor="center")

        get_balance_btn = Button(self, text="Посмотреть баланс", width=30, relief=RAISED)
        get_balance_btn.pack(side="top", pady=10, anchor="center")

        save_data_btn = Button(self, text="Сохранить", width=30, relief=RAISED)
        save_data_btn.pack(side="top", pady=10, anchor="center")

        load_data_btn = Button(self, text="Загрузить", width=30, relief=RAISED)
        load_data_btn.pack(side="top", pady=10, anchor="center")

    def open_transaction_window(self):
        """Открывает окно добавления новой транзакции"""
        if self.is_modal_opened:
            return
        self.is_modal_opened = True
        self.add_window = Toplevel(self)
        self.add_window.title("Добавить транзакцию")
        self.add_window.protocol("WM_DELETE_WINDOW", self.close_transaction_window)
        Label(self.add_window, text="Сумма:").grid(row=0, column=0, padx=5, pady=5)
        amount_entry = Entry(self.add_window)
        amount_entry.grid(row=0, column=1, pady=5, padx=5)

        Label(self.add_window, text="Категория:").grid(row=1, column=0, padx=5, pady=5)
        categories = ["Транспорт", "Еда", "Медицина", "Образование", "Досуг"]
        category_var = StringVar(value="")
        category_cmb = Combobox(self.add_window, values=categories, textvariable=category_var)
        category_cmb.grid(row=1, column=1, pady=5, padx=5)

        type_var = StringVar(value="Доход")
        Radiobutton(self.add_window, text="Доход", variable=type_var, value="Доход") \
            .grid(row=2, column=0, sticky="w")
        Radiobutton(self.add_window, text="Расход", variable=type_var, value="Расход") \
            .grid(row=2, column=1, sticky="w")

        Button(self.add_window, text="Сохранить", command=self.save_transaction) \
            .grid(row=3, column=0, columnspan=2, padx=5, pady=10)

    def close_transaction_window(self):
        self.is_modal_opened = False
        self.add_window.destroy()

    def save_transaction(self):
        self.add_window.destroy()
