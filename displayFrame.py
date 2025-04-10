from tkinter import Frame, Text, WORD


class DisplayFrame(Frame):

    def __init__(self, root):
        super().__init__(root)
        text_output = Text(self, wrap=WORD, state="disabled", bg="white", padx=10, pady=10)
        text_output.pack(expand=True, fill="both")

