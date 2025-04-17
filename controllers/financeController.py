from tkinter.messagebox import showerror

from models.fileManager import FileManager
from views.addWindow import AddWindow
from views.displayFrame import DisplayFrame
from models.financeManager import FinanceManager
from views.mainFrame import MainWindow
from views.navFrame import NavFrame


class FinanceController:
    is_modal_opened = False
    add_window = None

    def __init__(self):
        self.main_frame = MainWindow()

        self.display_frame = DisplayFrame(self.main_frame)
        self.display_frame.grid(column=1, row=0, sticky="nsew")

        self.nav_frame = NavFrame(self.main_frame, self)
        self.nav_frame.grid(column=0, row=0, sticky="nsew")

        self.finance_manager = FinanceManager(self.display_frame)
        self.file_manager = FileManager()

    def add_transaction(self):
        """Открывает окно добавления новой транзакции"""
        if self.is_modal_opened:
            return
        self.is_modal_opened = True
        self.add_window = AddWindow(self.nav_frame, self.save_transaction)
        self.add_window.protocol("WM_DELETE_WINDOW", self.close_transaction_window)

    def close_transaction_window(self):
        self.is_modal_opened = False
        self.add_window.destroy()

    def save_transaction(self):
        try:
            self.finance_manager.add_transaction(
                self.add_window.amount,
                self.add_window.category,
                self.add_window.type
            )
            self.finance_manager.show_transactions()
            self.close_transaction_window()
        except ValueError:
            showerror("Ошибка ввода!", 'Не заполнено поле "Сумма"', parent=self.add_window)

    def show_transactions(self):
        self.finance_manager.show_transactions()

    def show_balance(self):
        self.finance_manager.show_balance()

    def save(self):
        self.file_manager.save({
                "transactions": self.finance_manager.transactions,
                "balance": self.finance_manager.balance
            })

    def load(self):
        self.file_manager.load()

    def run(self):
        self.main_frame.mainloop()
