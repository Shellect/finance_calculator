from enum import Enum
from typing import List

from pydantic import BaseModel


class TransactionType(str, Enum):
    INCOME = "Доход"
    EXPENSE = "Расход"


class Transaction(BaseModel):
    amount: float
    category: str
    type: TransactionType


class FinanceData(BaseModel):
    transactions: List[Transaction] = []
    balance: float = 0.0
