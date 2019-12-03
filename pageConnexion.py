from tkinter import *
import tkinter.font as tkFont
from Assets.Ligne import *



class pageConnexion(Frame):
    def __init__(self, root):
        gris = '#333333'
        super().__init__(root, width=1080, height=720, bg=gris)
        self.root = root

        # Couleurs

        blanc = '#cccccc'
        blanc2 = '#e0e0e0'
        rouge = '#e84343'
        vert = '#1ece4d'
        bleuCase = '#4b4c5b'
        bleuSurligne = '#5b6982'
        grisClair = '#5e5e5e'

        # Polices d'ecriture
        fontTexte = tkFont.Font(family='Core Serif N 45 Medium', size=25)
        fontEntree = tkFont.Font(family='Core Serif N 45 Medium', size=15)
        fontRadio = tkFont.Font(family='Ubuntu', size=12, weight='bold')

        self.option_add("*Button.relief", FLAT)
        self.option_add("*Button.font", fontRadio)
        self.option_add("*Button.background", grisClair)
        self.option_add("*Button.foreground", blanc2)
        self.option_add("*Entry.font", fontEntree)
        self.option_add("*Entry.background", grisClair)
        self.option_add("*Entry.foreground", blanc2)
        self.option_add("*Entry.selectbackground", bleuSurligne)
        self.option_add("*Entry.relief", FLAT)
        self.option_add("*Label.justify", 'center')
        self.option_add("*Label.font", fontTexte)
        self.option_add("*Label.background", gris)
        self.option_add("*Label.foreground", blanc2)

        milieu = Frame(self, width=480, height=720, bg=gris)
        milieu.place(relx=0.5, rely=0.5, anchor=CENTER)

        accueil = Label(milieu, text='Connexion')
        accueil.place(relx=0.5, rely=0.18, anchor=CENTER)

        pseudo = Entry(milieu)
        pseudo.place(relx=0.5, rely=0.30, anchor=CENTER)

        texte = Frame(milieu, width=400, height=280, bg=grisClair)
        texte.place(relx=0.5, rely=0.40, anchor=N)

        texte2 = Frame(texte, width=400, height=280, bg=grisClair)
        texte2.grid(sticky='nesw')
        texte2.grid_propagate(0)

        contenuTexte = Tableau(texte2,[['Alexandre', 'Connecte'],['Leopold', 'En cours']])
        print(contenuTexte.listeLignes[0].listeCases[0].varTexte.get())
        contenuTexte.grid(sticky='nesw')
        contenuTexte.grid_propagate(0)
        contenuTexte.show()

        boutonValid = Button(milieu, text='Valider')
        boutonValid.place(relx=0.5, rely=0.90, anchor=CENTER)


if __name__ == '__main__':
    root = Tk()
    root.configure(background='#333333')

    test = pageConnexion(root)
    test.grid_propagate(0)
    test.place(relx=0.5, rely=0.5, anchor=CENTER)
    test.grid()

    root.mainloop()
