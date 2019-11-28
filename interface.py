from tkinter import *


class mainInterface(Frame):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        gris = '#333333'
        rouge = '#e84343'
        grisClair = '#5e5e5e'
        blanc = '#cccccc'
        blanc2 = '#e0e0e0'

        x = 0.05

        h = root.winfo_screenheight()
        w = root.winfo_screenwidth()

        entete = Canvas(bg='white', confine=TRUE)
        entete.place(relheight=x, relwidth=1 - x)

        carte = Frame(width=w / 4, height=h / 2, bg=blanc)
        carte.place(rely=2 * x, relx=1 - 0.25)

        bdp = Frame(bg=blanc2, width=(w * 3) / 4, height=h / 4)
        bdp.place(x=w - (w * 3 / 4), y=h - (h / 4))
