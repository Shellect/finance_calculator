from tkinter import Frame, Button
from tkinter.constants import RAISED


class NavFrame(Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.config(bg="white", bd=2, relief="groove")

        buttons = [
            {"text": "Добавить транзакцию", "command": controller.add_transaction},
            {"text": "Посмотреть транзакции", "command": controller.show_transactions},
            {"text": "Посмотреть баланс", "command": controller.show_balance},
            {"text": "Сохранить", "command": controller.save},
            {"text": "Загрузить", "command": controller.load},
        ]

        for button in buttons:
            Button(self, text=button["text"], width=30, relief=RAISED, command=button["command"]) \
                .pack(side="top", pady=15, anchor="center")
