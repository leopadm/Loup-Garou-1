from tkinter import Frame, StringVar, Label


class Case(Frame):
    def __init__(self, root, text="Default", coul="red"):
        self.coul = coul
        Frame.__init__(self, root, background="red")
        self.configure(bg=self.coul)
        self.varTexte = StringVar()
        self.varTexte.set(text)
        self.texte = Label(self, text=self.varTexte.get(), bg=coul)

    def setText(self, newValue):
        self.varTexte.set(newValue)

    def getText(self):
        retour = self.varTexte.get()
        return retour

    def reveal(self):
        self.texte.grid()


class Ligne(object):
    def __init__(self, listeDemandes: list, papa, color="white"):
        self.listeDemandes = listeDemandes
        self.listeCases = []
        for element in self.listeDemandes:
            self.listeCases.append(Case(text=element, root=papa, coul=color))


class Tableau(Frame):
    def __init__(self, papa, listeDemandesLignes: list, couleur1="#f7f7f7", couleur2="#e5e5e5"):
        Frame.__init__(self, papa)
        self.listeDemandesLignes = listeDemandesLignes
        self.listeLignes = []
        i = 1
        for element in self.listeDemandesLignes:
            if i % 2 == 0:
                couleur = couleur2
            else:
                couleur = couleur1
            self.listeLignes.append(Ligne(element, papa=self, color=couleur))
            i += 1

    def show(self):
        i = 0
        for ligne in self.listeLignes:
            j = 0
            for case in ligne.listeCases:
                print(case.coul)
                case.grid(row=i, column=j, sticky='nesw')
                case.reveal()
                j += 1
            i += 1
