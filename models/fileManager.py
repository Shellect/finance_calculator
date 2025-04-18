import pickle
from tkinter import filedialog, messagebox
import pandas as pd
import xml.etree.ElementTree as ET

from models.schemas import FinanceData, Transaction


class FileManager:
    def __init__(self, finance_manager):
        self.manager = finance_manager

    def save(self):
        """Сохраняет FinanceData в XML-файл."""
        filepath = filedialog.asksaveasfilename(defaultextension=".xml", filetypes=[("XML files", "*.xml")])
        if filepath:
            root = ET.Element("data")

            # Для каждой транзакции создаем строку в формате "amount=X category='Y' type=Z"
            for idx, transaction in enumerate(self.manager.transactions):
                row = ET.SubElement(root, "row")

                ET.SubElement(row, "index").text = str(idx)

                # Формируем строку транзакции
                trans_str = (
                    f"amount={transaction.amount} "
                    f"category='{transaction.category}' "
                    f"type=<TransactionType.{transaction.type.name}: '{transaction.type.value}'>"
                )
                ET.SubElement(row, "transactions").text = trans_str
                # Баланс (можно накапливать или использовать текущий)
                ET.SubElement(row, "balance").text = str(self.manager.balance)
            # Записываем в файл
            tree = ET.ElementTree(root)
            tree.write(filepath, encoding="utf-8", xml_declaration=True)
            messagebox.showinfo("Success!", "Данные успешно сохранены")

    def load(self):
        filepath = filedialog.askopenfilename(defaultextension=".xml", filetypes=[("XML files", "*.xml")])
        df = pd.read_xml(filepath)
        self.manager.data = FinanceData(transactions=[Transaction(**t) for t in df.transactions.to_dict()], balance=df.balance)
        messagebox.showinfo("Success!", "Данные успешно загружены")


    def backup(self):
        with open("backup", "wb") as fd:
            fd.write(pickle.dumps(self.manager))

    def restore(self):
        with open("backup", "rb") as fd:
            manager = pickle.load(fd)
            if manager:
                self.manager = manager
