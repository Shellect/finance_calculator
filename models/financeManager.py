class FinanceManager:
    """
    Управление финансовыми данными (транзакции, баланс)
    """
    def __init__(self, display_manager):
        self.__transactions = []
        self.__balance = 0.0
        self.display_manager = display_manager

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


    def show_transactions(self):
        self.display_manager.clear()
        for n, transaction in enumerate(self.transactions, 1):
            amount = transaction["amount"]
            category = transaction["category"]
            transaction_type = transaction["type"]
            self.display_manager.write_text(f"{n}. {transaction_type}: {amount} руб. ({category})\n")
        self.display_manager.disable()

    def show_balance(self):
        self.display_manager.clear()
        self.display_manager.write_text(f"текущий баланс: {self.balance} руб.\n")
        self.display_manager.disable()

    @property
    def transactions(self):
        return self.__transactions

    @property
    def balance(self):
        return self.__balance