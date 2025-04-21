from tkinter import filedialog, messagebox
from xml.etree.ElementTree import SubElement, Element, ElementTree, parse

from models.schemas import FinanceData, Transaction, TransactionType


class FileManager:

    @staticmethod
    def save(finance_data: FinanceData) -> None:
        """Сохраняет FinanceData в XML-файл."""
        file_path = filedialog.asksaveasfilename(defaultextension=".xml", filetypes=[("XML files", "*.xml")])
        if file_path:
            root = Element("data")

            # Сохраняем баланс
            SubElement(root, "balance").text = str(finance_data.balance)

            # Контейнер для транзакций
            transactions_elem = SubElement(root, "transactions")

            for transaction in finance_data.transactions:
                trans_elem = SubElement(transactions_elem, "transaction")
                SubElement(trans_elem, "amount").text = str(transaction.amount)
                SubElement(trans_elem, "category").text = transaction.category
                SubElement(trans_elem, "type").text = transaction.type.name  # "EXPENSE" или "INCOME"

            # Записываем в файл
            tree = ElementTree(root)
            tree.write(file_path, encoding="utf-8", xml_declaration=True)
            messagebox.showinfo("Success!", "Данные успешно сохранены")

    @staticmethod
    def load(finance_data: FinanceData) -> None:
        file_path = filedialog.askopenfilename(defaultextension=".xml", filetypes=[("XML files", "*.xml")])
        if file_path:
            tree = parse(file_path)
            root = tree.getroot()

            transactions = []

            for trans_elem in root.find("transactions").findall("transaction"):
                amount = float(trans_elem.find("amount").text)
                category = trans_elem.find("category").text
                trans_type = TransactionType[trans_elem.find("type").text]  # Преобразуем строку в enum

                transactions.append(Transaction(
                    amount=amount,
                    category=category,
                    type=trans_type
                ))

            messagebox.showinfo("Success!", "Данные успешно загружены")
            finance_data.transactions = transactions
