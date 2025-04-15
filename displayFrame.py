from tkinter import Frame, Text, WORD, END


class DisplayFrame(Frame):

    def __init__(self, root):
        super().__init__(root)
        self.text_output = Text(self, wrap=WORD, state="disabled", bg="white", padx=10, pady=10)
        self.text_output.pack(expand=True, fill="both")

    def show_transactions(self, transactions):
        self.text_output.config(state="normal")
        self.text_output.delete(1.0, END)

        for n, transaction in enumerate(transactions, 1):
            amount = transaction["amount"]
            category = transaction["category"]
            transaction_type = transaction["type"]
            self.text_output.insert(END, f"{n}. {transaction_type}: {amount} руб. ({category})\n")
        self.text_output.config(state="disabled")
