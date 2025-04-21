from tkinter import Toplevel, StringVar
from tkinter.ttk import Label, Entry, Combobox, Radiobutton, Button

from models.schemas import Transaction, TransactionType


class TransactionAppendWindow(Toplevel):
    modal_width = 300
    modal_height = 150

    def __init__(self, frame, command):
        super().__init__(frame)
        x = round(self.winfo_screenwidth() / 2 - self.modal_width / 2)
        y = round(self.winfo_screenheight() / 2 - self.modal_height / 2)
        self.geometry(f"{self.modal_width}x{self.modal_height}+{x}+{y}")

        self.title("Добавить транзакцию")
        Label(self, text="Сумма:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.amount_entry = Entry(self)
        self.amount_entry.grid(row=0, column=1, pady=5, padx=5, sticky="w")

        Label(self, text="Категория:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        categories = ["Транспорт", "Еда", "Медицина", "Образование", "Досуг"]
        self.category_var = StringVar(value="")
        category_cmb = Combobox(self, values=categories, textvariable=self.category_var)
        category_cmb.grid(row=1, column=1, pady=5, padx=5, sticky="w")

        self.type_var = StringVar(value="Доход")
        Radiobutton(self, text="Доход", variable=self.type_var, value="Доход") \
            .grid(row=2, column=1, sticky="w")
        Radiobutton(self, text="Расход", variable=self.type_var, value="Расход") \
            .grid(row=3, column=1, sticky="w")

        Button(self, text="Сохранить", command=command) \
            .grid(row=4, column=0, columnspan=2, pady=10)

    @property
    def transaction(self) -> Transaction:
        return Transaction(
            amount=float(self.amount_entry.get().replace(",", ".")),
            category=self.category_var.get(),
            type=TransactionType(self.type_var.get())
        )
