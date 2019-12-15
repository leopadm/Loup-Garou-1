from tkinter import *
import tkinter.font as tkFont
from tchatVillageClient import *

log1 = 'testvillage'
log2 = 'testmorts'
log3 = 'testloups'
dictionnaire = {'Village': log1, 'Morts': log2, 'Loups': log3}

# Couleurs
gris = '#333333'
blanc = '#cccccc'
blanc2 = '#e0e0e0'
rouge = '#e84343'
vert = '#1ece4d'
bleuCase = '#4b4c5b'
bleuSurligne = '#5b6982'
grisClair = '#5e5e5e'

fenetre = Tk()

# Polices d'ecriture
fontRadio = tkFont.Font(family='Ubuntu', size=12, weight = 'bold')
fontTexte = tkFont.Font(family='Core Serif N 45 Medium', size=15)
fontEntree = tkFont.Font(family='Core Serif N 45 Medium', size=15)

# Options
fenetre.option_add("*Label.justify", 'center')
fenetre.option_add("*Label.font", fontTexte)
fenetre.option_add("*Label.background", gris)
fenetre.option_add("*Label.foreground", blanc2)
fenetre.option_add("*Text.font", fontEntree)
fenetre.option_add("*Text.background", grisClair)
fenetre.option_add("*Text.foreground", blanc2)
fenetre.option_add("*Text.selectbackground", bleuSurligne)
fenetre.option_add("*Text.relief", FLAT)
fenetre.option_add("*Button.relief", FLAT)
fenetre.option_add("*Button.font", fontRadio)
fenetre.option_add("*Button.background", grisClair)
fenetre.option_add("*Button.foreground", blanc2)

listeOptions = ('Village', 'Morts', 'Loups')
v = StringVar()
v.set(listeOptions[0])
om = OptionMenu(fenetre, v, *listeOptions)
om.pack()

texte = Label(fenetre, text=v.get())
texte.pack()

om.bind('<Configure> ', lambda event: texte.config(text=dictionnaire[v.get()]))


fenetre.mainloop()
