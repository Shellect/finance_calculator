from models.fileManager import FileManager
from views.displayFrame import DisplayFrame
from models.financeManager import FinanceManager
from views.mainFrame import MainWindow
from views.navFrame import NavFrame


class FinanceController:

    def __init__(self):
        self.main_frame = MainWindow()
        self.finance_manager = FinanceManager()

        display_frame = DisplayFrame(self.main_frame)
        display_frame.grid(column=1, row=0, sticky="nsew")
        self.finance_manager.add_observer(display_frame)

        self.nav_frame = NavFrame(self.main_frame, {
            "add_transaction": self.add_transaction,
            "show_transactions": self.show_transactions,
            "show_balance": self.show_balance,
            "load_data": self.load_data,
            "save_data": self.save_data,
        })
        self.nav_frame.grid(column=0, row=0, sticky="nsew")

    def add_transaction(self):
        self.finance_manager.show_transaction_window(self.nav_frame)

    def show_transactions(self):
        self.finance_manager.show_transactions()

    def show_balance(self):
        self.finance_manager.show_balance()

    def save_data(self):
        FileManager.save(self.finance_manager.finance_data)

    def load_data(self):
        FileManager.load(self.finance_manager.finance_data)

    def run(self):
        self.main_frame.mainloop()
