from models.schemas import FinanceData, Transaction, TransactionType


class DataStorage:
    def __init__(self):
        self._data = FinanceData()

    @property
    def data(self) -> FinanceData:
        return self._data.model_copy()

    def add_transaction(self, amount, category, transaction_type):
        if transaction_type == "Расход":
            self._data.balance -= amount
        elif transaction_type == "Доход":
            self._data.balance += amount
        self._data.transactions.append(Transaction(amount=amount, category=category, type=TransactionType(transaction_type)))