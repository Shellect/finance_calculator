from enum import Enum
from typing import List, Type

from pydantic import BaseModel, computed_field


class TransactionType(str, Enum):
    INCOME = "Доход"
    EXPENSE = "Расход"


class Transaction(BaseModel):
    amount: float
    category: str
    type: TransactionType | Type[TransactionType]


class FinanceData(BaseModel):
    transactions: List[Transaction] = []

    @computed_field
    def balance(self) -> float:
        balance = 0.0
        for transaction in self.transactions:
            if transaction.type == TransactionType.EXPENSE:
                balance -= transaction.amount
            elif transaction.type == TransactionType.INCOME:
                balance += transaction.amount
        return balance
