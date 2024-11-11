# importing tkinter module
from tkinter import *


class NewWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.worstWindow = Toplevel(self.master.root)
        self.worstWindow.title("Tilføje Navn")
        self.worstWindow.geometry("200x200")

        Label(self.worstWindow,
              text="Tilføje navn").pack()

        self.nynavn = Entry(self.worstWindow)
        self.nynavn.pack()
        self.button = Button(self.worstWindow, text="tilføje navn", command=self.nynavn)


    def nynavn(self,master):
        try:
            navn = abs(int(self.nynavn))
        except:
            messagebox.showerror(parent=self.worstWindow, titel="tilføjelse fejl", message="prøv igen.\nGenstart window")

    def handle_button_press(self, event):
            self.destroy()


    #def addMoney(self):
       # try:
     #       amount = abs(int(self.money.get())) #HUSK AT VALIDERE INPUT!, kun positive heltal!
      #  except:
       #     messagebox.showerror(parent=self.payWindow , title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
        #    return
#
 #       self.master.total += amount
  #      self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
   #     print(f"Indsamlet: {self.master.total} af {self.master.target} kroner!")
    #    self.master.progress['value'] = self.master.total / self.master.target * 100
            self.master.gemFilen()