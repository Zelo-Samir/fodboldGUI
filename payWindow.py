# importing tkinter module
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
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

        self.variable = StringVar()
        self.variable.set(OPTIONS[0])
        self.optionMenu = OptionMenu(self.payWindow, self.variable, *OPTIONS)
        self.optionMenu.pack()
        self.button.pack()

        img = ImageTk.PhotoImage(Image.open("assets/img/kyriakos.jpg"))
        panel = Label(self.payWindow, image=img)
        panel.image = img
        panel.pack(side="bottom", fill="both")

    def gemFilen(self):
        outfile = open(self.filename, 'wb')
        pickle.dump(self.fodboldtur, outfile)
        outfile.close()
        print("GEMT")

    def addMoney(self):
        try:
            amount = int(self.money.get()) #HUSK AT VALIDERE INPUT!, kun positive heltal!
        except:
            messagebox.showerror(parent=self.payWindow , title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
            return

        #self.fodboldtur[str(self.variable)] += self.money.get()

        # Get the selected key from the OptionMenu
        selected_key = self.variable.get()

        # Update the dictionary
        if selected_key in self.fodboldtur:
            self.fodboldtur[selected_key] += amount
        else:
            messagebox.showerror(parent=self.payWindow, title="Fejl!", message="Valgt nøgle findes ikke!")
            return

        self.master.total += amount
        self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
        print(f"Indsamlet: {self.master.total} af {self.master.target} kroner!")
        self.master.progress['value'] = self.master.total / self.master.target * 100
        ##TODO: TELL MAIN WINDOW TO PICKLE THE DICTIONARY
        self.gemFilen()
