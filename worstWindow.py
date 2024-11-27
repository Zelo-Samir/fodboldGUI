# importing tkinter module
from tkinter import *
from tkinter import messagebox
import pickle

class NewWindowClass:
    def __init__(self, master):
        # load filen:
        self.filename = 'betalinger.pk'
        self.fodboldtur = {}
        try:  # FILEN FINDES :)
            infile = open(self.filename, 'rb')
            self.fodboldtur = pickle.load(infile)
            infile.close()
        except:  # FILEN FINDES IKKE.
            print("Samir der er en fejl")
            pass


        self.master = master #reference til main window objektet
        self.worstWindow = Toplevel(self.master.root)
        self.worstWindow.title("Tilføje Navn")
        self.worstWindow.geometry("200x200")

        Label(self.worstWindow,
              text="Tilføje navn").pack()

        self.nynavn = Entry(self.worstWindow)
        self.nynavn.pack()
        self.button = Button(self.worstWindow, text="tilføj", command=self.tilføjnavn)
        self.button.pack()

    def gemFilen(self):
        outfile = open(self.filename, 'wb')
        pickle.dump(self.fodboldtur, outfile)
        outfile.close()
        print("GEMT")

    def tilføjnavn(self):
        self.fodboldtur[self.nynavn.get()] = 0
        self.gemFilen()
