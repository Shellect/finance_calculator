from typing import Callable
from tkinter import Frame, Button


class NavFrame(Frame):
    def __init__(self, root, controller_callbacks: dict[str, Callable]):
        super().__init__(root, bg="white", bd=2, relief="groove")

        buttons = [
            {"text": "Добавить транзакцию", "command": controller_callbacks["add_transaction"]},
            {"text": "Посмотреть транзакции", "command": controller_callbacks["show_transactions"]},
            {"text": "Посмотреть баланс", "command": controller_callbacks["show_balance"]},
            {"text": "Сохранить", "command": controller_callbacks["save_data"]},
            {"text": "Загрузить", "command": controller_callbacks["load_data"]},
        ]

        for button in buttons:
            Button(self, text=button["text"], width=30, relief="raised", command=button["command"]) \
                .pack(side="top", pady=15, anchor="center")
