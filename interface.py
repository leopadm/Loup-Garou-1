from tkinter import *
from pageConnexion import jouer


def intermediaire():
    main.destroy()
    jouer()


gris = '#333333'
rouge = '#e84343'
x = 0.05
main = Tk()
main.config(bg=gris)
main.attributes('-fullscreen', 1)
quitter = Button(main, text="Quit", command=main.destroy, bg=rouge, activebackground=rouge, cursor='hand2', borderwidth=0, highlightthickness=0)
quitter.place(relheight=x, relwidth=x, relx=1-x, rely=0)
quitter.bind('<buttonpress-1')

entete = Canvas(bg='white')
entete.place(relheight=x, relwidth=1-x)

go = Button(main, text='Lancer le jeu', command=intermediaire, cursor='hand2', borderwidth=0, highlightthickness=0)
go.place(relheight=x, relwidth=x, relx=0.5-x/2, rely=0.5-x/2)
go.bind('<buttonpress-1')

main.mainloop()
