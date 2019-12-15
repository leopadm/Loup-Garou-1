from tkinter import *
from PIL import Image, ImageTk


class mainInterface(Frame):

    def __init__(self, root, player):
        super().__init__(root)
        self.root = root
        gris = '#333333'
        rouge = '#e84343'
        grisClair = '#5e5e5e'
        blanc = '#cccccc'
        blanc2 = '#e0e0e0'

        # Initialisation de donnees
        h = root.winfo_screenheight()
        w = root.winfo_screenwidth()
        relx = 0.05

        # Background
        vil = Image.open("game_background_day.jpg")
        village1 = vil.resize((w, h), Image.ANTIALIAS)
        village = ImageTk.PhotoImage(village1)

        #Creation de l'espace pour le background
        fond = Label(root, bg=gris, width=w, height=h, image=village)
        fond.image = village
        fond.pack()

        # Creation de l'espace pour la timeline
        entete = Frame(bg='white', bd=0)
        entete.place(relheight=relx, relwidth=1 - relx)

        # Carte joueur
        im = Image.open(player)
        im1 = im.resize((int(h/2), int(h/2)), Image.ANTIALIAS)
        carte = ImageTk.PhotoImage(im1)

        # Creation de l'espace pour la carte du joueur
        cartejoueur = Label(root, width=h / 2, height=h / 2, bg='black', image=carte)
        cartejoueur.image = carte
        cartejoueur.place(rely=3 * relx / 2, relx=(3 / 4) - relx)

        # creation de l'espace pour les actions du joueur
        widget = Frame(bg=blanc2, width=((w * 3) / 4), height=(h / 4))
        widget.place(relx=(1 / 4), rely=0.75 - relx)
        # widget.attributes('-alpha', 1)

        # Creation du boutton pour fermer la fenetre
        quitter = Button(root, text="Quit", bg=rouge, activebackground=rouge, cursor='hand2', borderwidth=0, highlightthickness=0)
        quitter.place(relheight=relx, relwidth=relx, relx=1 - relx, rely=0)
        quitter.bind('<Button-1>', lambda event: root.destroy())

