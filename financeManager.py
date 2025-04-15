class FinanceManager:
    """
    Управление финансовыми данными (транзакции, баланс)
    """
    def __init__(self):
        self.__transactions = []
        self.__balance = 0.0

    def add_transaction(self, amount, category, transaction_type):
        if transaction_type == "Расход":
            self.__balance -= amount
        elif transaction_type == "Доход":
            self.__balance += amount
        self.__transactions.append({
            "amount": amount,
            "category": category,
            "type": transaction_type
        })

    @property
    def transactions(self):
        return self.__transactions

    @property
    def balance(self):
        return self.__balance