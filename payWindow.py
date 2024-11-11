# importing tkinter module
from tkinter import *
from tkinter import messagebox
import pickle

class payWindowClass:

    def __init__(self, master):
        self.master = master #reference til main window objektet

        # load filen:
        self.filename = 'betalinger.pk'
        self.fodboldtur = {}
        try:  # FILEN FINDES :)
            infile = open(self.filename, 'rb')
            self.fodboldtur = pickle.load(infile)
            infile.close()
        except:  # FILEN FINDES IKKE.
            messagebox.showerror(parent=self.master.root, title="GWAAAAAAA", message="FILEN ER IKKE FUNDET!!")


        self.payWindow = Toplevel(self.master.root)
        self.payWindow.title("Indbetaling")
        self.payWindow.geometry("200x200")

        Label(self.payWindow,
              text="Indbetal").pack()

        self.money = Entry(self.payWindow)
        self.money.pack()
        self.button = Button(self.payWindow, text="Betal", command= self.addMoney)

        OPTIONS = []
        for key, value in self.fodboldtur.items():
            OPTIONS.append(key)

        variable = StringVar()
        variable.set(OPTIONS[0])
        self.optionMenu = OptionMenu(self.payWindow, variable, *OPTIONS)
        self.optionMenu.pack()
        self.button.pack()

    def addMoney(self):
        try:
            amount = abs(int(self.money.get())) #HUSK AT VALIDERE INPUT!, kun positive heltal!
        except:
            messagebox.showerror(parent=self.payWindow , title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
            return

        self.fodboldtur[self.optionMenu.]
        self.master.total += amount
        self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
        print(f"Indsamlet: {self.master.total} af {self.master.target} kroner!")
        self.master.progress['value'] = self.master.total / self.master.target * 100
        ##TODO: TELL MAIN WINDOW TO PICKLE THE DICTIONARY
        self.master.gemFilen()