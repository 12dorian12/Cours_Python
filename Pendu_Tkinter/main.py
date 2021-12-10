import tkinter as tk

import Pendu as p

root = tk.Tk()

frm_start = tk.Frame(root)
frm_start.grid()
frm_jeu = tk.Frame(root)
frm_gagner = tk.Frame(root)
frm_perdu = tk.Frame(root)

jeu = p.Pendu(frm_start, frm_jeu, frm_gagner, frm_perdu)

tk.Label(frm_start, text="Entre le mot mystere : ").grid(column=0, row=0)

start_entry = tk.Entry(frm_start, text="")
start_entry.grid(column=1, row=0)

tk.Button(frm_start, text="Aleatoire", command= jeu.lance_jeu_rnd).grid(column=0, row=1)
tk.Button(frm_start, text="Valider", command= lambda : jeu.lance_jeu(start_entry.get())).grid(column=1, row=1)
tk.Button(frm_start, text="Quiter", command=root.destroy).grid(column=2, row=1)










can = tk.Canvas(frm_jeu, height=300, width=300)
can.grid(column=0, row=0, rowspan = 3)
jeu.set_canvas(can)

jeu_mot = tk.Label(frm_jeu)
jeu_mot.grid(column=1, row=0)
jeu.set_mot(jeu_mot)

jeu_vie = tk.Label(frm_jeu)
jeu_vie.grid(column=1, row=1)
jeu.set_vie(jeu_vie)


jeu_entry = tk.Entry(frm_jeu, text="")
jeu_entry.grid(column=1, row=2)

tk.Button(frm_jeu, text="Valider", command=lambda : jeu.verif_mot(jeu_entry.get())).grid(column=1, row=4)
tk.Button(frm_jeu, text="Quiter", command=root.destroy).grid(column=0, row=4)












tk.Label(frm_gagner, text="Gagner").grid(column=0, row=0)
tk.Button(frm_gagner, text="Quiter", command=root.destroy).grid(column=0, row=4)








tk.Label(frm_perdu, text="Perdu").grid(column=0, row=0)
tk.Button(frm_perdu, text="Quiter", command=root.destroy).grid(column=0, row=4)


root.mainloop()
