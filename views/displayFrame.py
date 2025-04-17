from tkinter import Frame, Text, WORD, END


class DisplayFrame(Frame):

    def __init__(self, root):
        super().__init__(root)
        self.text_output = Text(self, wrap=WORD, state="disabled", bg="white", padx=10, pady=10)
        self.text_output.pack(expand=True, fill="both")

    def clear(self):
        self.text_output.config(state="normal")
        self.text_output.delete(1.0, END)

    def write_text(self, row):
        self.text_output.insert(END, row)

    def disable(self):
        self.text_output.config(state="disabled")


