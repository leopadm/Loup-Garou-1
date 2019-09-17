from tkinter import *

log1 = 'testvillage'
log2 = 'testmorts'
log3 = 'testloups'
dictionnaire = {'Village': log1, 'Morts': log2, 'Loups': log3}


root = Tk()

listeOptions = ('Village', 'Morts', 'Loups')
v = StringVar()
v.set(listeOptions[0])
om = OptionMenu(root, v, *listeOptions)
om.pack()

texte = Label(root, text=v.get())
texte.pack()

om.bind('<Configure> ', lambda event: texte.config(text=dictionnaire[v.get()]))

root.mainloop()
