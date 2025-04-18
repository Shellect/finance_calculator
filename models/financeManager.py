from tkinter.messagebox import showerror
from typing import Protocol

from models.storage import DataStorage
from views.transactionAppendWindow import TransactionAppendWindow


class Observer(Protocol):
    def refresh(self, text: str) -> None: ...


class FinanceManager:
    """
    Управление финансовыми данными (транзакции, баланс)
    """

    def __init__(self):
        self._observers: list[Observer] = []
        self.storage = DataStorage()

        self.is_modal_open = False
        self.transaction_append_window = None

    def add_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def notify_observers(self, text: str) -> None:
        for observer in self._observers:
            observer.refresh(text)

    def show_transaction_window(self, nav_frame):
        """Открывает окно добавления новой транзакции"""
        if self.is_modal_open:
            return
        self.is_modal_open = True
        self.transaction_append_window = TransactionAppendWindow(nav_frame, self.save_transaction)
        self.transaction_append_window.protocol("WM_DELETE_WINDOW", self.close_transaction_window)

    def close_transaction_window(self):
        self.is_modal_open = False
        self.transaction_append_window.destroy()

    def save_transaction(self):
        try:
            self.storage.add_transaction(
                self.transaction_append_window.amount,
                self.transaction_append_window.category,
                self.transaction_append_window.type
            )
            self.show_transactions()
            self.close_transaction_window()
        except ValueError:
            showerror("Ошибка ввода!", 'Не заполнено поле "Сумма"', parent=self.transaction_append_window)

    def show_transactions(self):
        transactions = self.transactions
        if not transactions:
            text = "Нет транзакций"
        else:
            text = ""
            for n, transaction in enumerate(transactions, 1):
                text += f"{n}. {transaction.type}: {transaction.amount} руб. ({transaction.category})\n"
        self.notify_observers(text)

    def show_balance(self):
        self.notify_observers(f"Текущий баланс: {self.balance} руб.\n")

    @property
    def transactions(self):
        return self.storage.data.transactions

    @property
    def balance(self):
        return self.storage.data.balance
