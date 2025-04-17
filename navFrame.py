from tkinter import Frame, Button, Toplevel, Label, Entry, StringVar
from tkinter.ttk import Radiobutton, Combobox
from tkinter.messagebox import showerror
from tkinter.constants import RAISED

from fileManager import FileManager
from financeManager import FinanceManager


class NavFrame(Frame):
    is_modal_opened = False
    modal_width = 300
    modal_height = 150

    def __init__(self, root, main_frame):
        super().__init__(root)
        self.finance_manager = FinanceManager()
        self.file_manager = FileManager(self.finance_manager)
        self.main_frame = main_frame
        self.type_var = StringVar(value="Доход")
        self.category_var = StringVar(value="")
        self.add_window = None
        self.amount_entry = None
        self.config(bg="white", bd=2, relief="groove")

        add_transaction_btn = Button(self, text="Добавить транзакцию", width=30, relief=RAISED,
                                     command=self.open_transaction_window)
        add_transaction_btn.pack(side="top", pady=15, anchor="center")

        get_transactions_btn = Button(self, text="Посмотреть транзакции", width=30, relief=RAISED)
        get_transactions_btn.pack(side="top", pady=15, anchor="center")

        get_balance_btn = Button(self, text="Посмотреть баланс", width=30, relief=RAISED)
        get_balance_btn.pack(side="top", pady=10, anchor="center")

        save_data_btn = Button(self, text="Сохранить", width=30, relief=RAISED, command=self.file_manager.save)
        save_data_btn.pack(side="top", pady=10, anchor="center")

        load_data_btn = Button(self, text="Загрузить", width=30, relief=RAISED)
        load_data_btn.pack(side="top", pady=10, anchor="center")

    def open_transaction_window(self):
        """Открывает окно добавления новой транзакции"""
        if self.is_modal_opened:
            return
        self.is_modal_opened = True
        self.add_window = Toplevel(self)
        x = round(self.add_window.winfo_screenwidth() / 2 - self.modal_width / 2)
        y = round(self.add_window.winfo_screenheight() / 2 - self.modal_height / 2)
        self.add_window.geometry(f"{self.modal_width}x{self.modal_height}+{x}+{y}")
        self.add_window.title("Добавить транзакцию")
        self.add_window.protocol("WM_DELETE_WINDOW", self.close_transaction_window)

        Label(self.add_window, text="Сумма:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.amount_entry = Entry(self.add_window)
        self.amount_entry.grid(row=0, column=1, pady=5, padx=5, sticky="w")

        Label(self.add_window, text="Категория:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        categories = ["Транспорт", "Еда", "Медицина", "Образование", "Досуг"]
        category_cmb = Combobox(self.add_window, values=categories, textvariable=self.category_var)
        category_cmb.grid(row=1, column=1, pady=5, padx=5, sticky="w")

        Radiobutton(self.add_window, text="Доход", variable=self.type_var, value="Доход") \
            .grid(row=2, column=1, sticky="w")
        Radiobutton(self.add_window, text="Расход", variable=self.type_var, value="Расход") \
            .grid(row=3, column=1, sticky="w")

        Button(self.add_window, text="Сохранить", command=self.save_transaction) \
            .grid(row=4, column=0, columnspan=2, pady=10)

    def close_transaction_window(self):
        self.is_modal_opened = False
        self.add_window.destroy()

    def save_transaction(self):
        try:
            amount = float(self.amount_entry.get().replace(",", "."))
            self.finance_manager.add_transaction(amount, self.category_var.get(), self.type_var.get())
            self.main_frame.show_transactions(self.finance_manager.transactions)
            self.close_transaction_window()
            self.file_manager.backup()
        except ValueError:
            showerror("Ошибка ввода!", 'Не заполнено поле "Сумма"', parent=self.add_window)

