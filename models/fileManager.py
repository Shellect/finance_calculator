from tkinter import filedialog, messagebox
import pandas as pd


class FileManager:
    def save(self, data):
        filepath = filedialog.asksaveasfilename(defaultextension=".xml", filetypes=[("XML files", "*.xml")])
        if filepath:
            df = pd.DataFrame(data)
            df.to_xml(filepath)
            messagebox.showinfo("Success!", "Данные успешно сохранены")

    def load(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".xml", filetypes=[("XML files", "*.xml")])

    # def backup(self):
