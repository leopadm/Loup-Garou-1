from tkinter import *

gris = '#333333'
rouge = '#e84343'
grisClair = '#5e5e5e'
blanc = '#cccccc'
blanc2 = '#e0e0e0'

x = 0.05
main = Tk()
main.config(bg=gris)
main.attributes('-fullscreen', 1)
main.mainloop()
quitter = Button(main, text="Quit", bg=rouge, activebackground=rouge, cursor='hand2', borderwidth=0, highlightthickness=0)
quitter.place(relheight=x, relwidth=x, relx=1-x, rely=0)
quitter.bind('<Button-1>', lambda event: main.destroy())

h = main.winfo_screenheight()
w = main.winfo_screenwidth()


class mainInterface(Frame):
    def __init__(self, root):
        Frame.__init__(root)
        gris = '#333333'
        rouge = '#e84343'
        grisClair = '#5e5e5e'
        blanc = '#cccccc'
        blanc2 = '#e0e0e0'

        h = root.winfo_screenheight()
        w = root.winfo_screenwidth()

        entete = Canvas(bg='white', confine=TRUE)
        entete.place(relheight=x, relwidth=1-x)

        carte = Frame(width=w/4, height=h/2, bg=blanc)
        carte.place(rely=2*x, relx=1-0.25)

        bdp = Frame(bg=blanc2, width=(w*3)/4, height=h/4)
        bdp.place(x=w-(w*3/4), y=h-(h/4))





