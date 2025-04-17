from tkinter import filedialog, messagebox
import pandas as pd
import pickle

from financeManager import FinanceManager


class FileManager:
    def __init__(self, finance_manager: FinanceManager):
        self.manager = finance_manager

    def save(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".xml", filetypes=[("XML files", "*.xml")])
        if filepath:
            data = {
                "transactions": self.manager.transactions,
                "balance": self.manager.balance
            }
            df = pd.DataFrame(data)
            df.to_xml(filepath)
            messagebox.showinfo("Success!", "Данные успешно сохранены")

    def load(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".xml", filetypes=[("XML files", "*.xml")])

    def backup(self):
        with open("backup", "wb") as fd:
            fd.write(pickle.dumps(self.manager))

    def restore(self):
        with open("backup", "rb") as fd:
            manager = pickle.load(fd)
            if manager:
                self.manager = manager