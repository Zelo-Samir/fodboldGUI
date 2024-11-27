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
            pass
            # messagebox.showerror(parent=self.root, title="GWAAAAAAA", message="FILEN ER IKKE FUNDET!!")

        self.master = master  # reference til main window objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("500x500")

        Label(self.listWindow, text="Liste over indbetalinger", font="bold").grid(row=0, column=0, columnspan=3)

        self.list = Text(self.listWindow, height=20, width=50, padx=5)
        self.list.grid(row=1, column=0, columnspan=3)

        # Liste over de tre værste medlammer
        listemindst = []
        self.listemindstnavn = []

        #TODO: Fiks denne funktion
        for item in self.fodboldtur.items():

            if item[1] >= 4500:
                pass
            else:
                if len(listemindst) > 3:
                    for number in listemindst:
                        if item[1] < number:
                            self.listemindstnavn.append(item[0])
                            self.listemindstnavn.remove(number)
                else:
                    self.listemindstnavn.append(item[0])

        self.worstlist = Text(self.listWindow, height=5, width=50, padx=5, pady=20)
        self.worstlist.grid(row=2, column=0, columnspan=3)

        print(self.listemindstnavn)
        self.update()

    def update(self):
        total = 0
        self.worstlist.insert(END, f"Top tre værste betalere: \n\n")

        for item in self.fodboldtur.items():
            self.list.insert(END, f"{item[0]} har betalt {item[1]} kr\n")
            total += item[1]

            # væreste liste
            if item[0] in self.listemindstnavn:
                self.worstlist.insert(END, f"{item[0]} mangler at betale {4500 - item[1]}\n")

        self.list.insert(END, f"\n Totalt: {total} kr")
