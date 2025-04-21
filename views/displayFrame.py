from tkinter import Frame, Text, END


class DisplayFrame(Frame):

    def __init__(self, root):
        super().__init__(root)
        self.text_output = Text(self, wrap="word", state="disabled", bg="white", padx=10, pady=10)
        self.text_output.pack(expand=True, fill="both")

    def refresh(self, text: str):
        self.text_output.config(state="normal")
        self.text_output.delete(1.0, END)
        self.text_output.insert(END, text)
        self.text_output.config(state="disabled")
