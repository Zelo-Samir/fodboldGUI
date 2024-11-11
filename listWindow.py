# importing tkinter module
from tkinter import *
import pickle


class ListWindowClass:

    def __init__(self, master):

        # load filen:
        self.filename = 'betalinger.pk'
        self.fodboldtur = {}
        try:  # FILEN FINDES :)
            infile = open(self.filename, 'rb')
            self.fodboldtur = pickle.load(infile)
            infile.close()
        except:  # FILEN FINDES IKKE.
            messagebox.showerror(parent=self.root, title="GWAAAAAAA", message="FILEN ER IKKE FUNDET!!")

        self.master = master  # reference til main window objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("500x500")

        Label(self.listWindow, text="Liste over indbetalinger", font="bold").grid(row=0, column=0, columnspan=3)

        self.list = Text(self.listWindow, height=10, width=50, padx=5)
        self.list.grid(row=1, column=0, columnspan=3)

        self.update()

    def update(self):
        total = 0
        for item in self.fodboldtur.items():
            self.list.insert(END, f"{item[0]} har betalt {item[1]} kr\n")
            total += item[1]
        self.list.insert(END, f"\n Totalt: {total} kr")
