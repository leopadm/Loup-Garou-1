from tkinter import *
from interface import mainInterface

gris = '#333333'


def lancement():
    x = 0.05
    main = Tk()
    main.config(bg=gris)
    main.attributes('-fullscreen', 1)

    mainInterface(main, 'chasseur.png')
    main.mainloop()
