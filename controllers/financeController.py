from models.fileManager import FileManager
from views.displayFrame import DisplayFrame
from models.financeManager import FinanceManager
from views.mainFrame import MainWindow
from views.navFrame import NavFrame


class FinanceController:

    def __init__(self):
        self.main_frame = MainWindow()
        self.finance_manager = FinanceManager()
        self.file_manager = FileManager(self.finance_manager)

        display_frame = DisplayFrame(self.main_frame)
        display_frame.grid(column=1, row=0, sticky="nsew")
        self.finance_manager.add_observer(display_frame)

        self.nav_frame = NavFrame(self.main_frame, self)
        self.nav_frame.grid(column=0, row=0, sticky="nsew")

    def add_transaction(self):
        self.finance_manager.show_transaction_window(self.nav_frame)

    def show_transactions(self):
        self.finance_manager.show_transactions()

    def show_balance(self):
        self.finance_manager.show_balance()

    def save(self):
        self.file_manager.save()

    def load(self):
        self.file_manager.load()

    def run(self):
        self.main_frame.mainloop()
