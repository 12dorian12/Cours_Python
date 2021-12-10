import random as rnd
import tkinter as tk

class Pendu():
    def __init__(self, frame_start, frame_jeu, frame_gagner, frame_perdu):
        self.__frame_start = frame_start
        self.__frame_jeu = frame_jeu
        self.__frame_gagner = frame_gagner
        self.__frame_perdu = frame_perdu

        self.__mot_mystere = None
        self.__canvas = None
        self.__label_mot = None
        self.__label_vie = None
        self.__lettre_dite = []

        self.__liste_mot = open(__file__[0:-8]+"media/liste_francais_sans-accent.txt", "r").readlines()

        self.__images = []
        self.__images.append(tk.PhotoImage(file=__file__[0:-8]+"media/img/bonhomme1.gif"))
        self.__images.append(tk.PhotoImage(file=__file__[0:-8]+"media/img/bonhomme2.gif"))
        self.__images.append(tk.PhotoImage(file=__file__[0:-8]+"media/img/bonhomme3.gif"))
        self.__images.append(tk.PhotoImage(file=__file__[0:-8]+"media/img/bonhomme4.gif"))
        self.__images.append(tk.PhotoImage(file=__file__[0:-8]+"media/img/bonhomme5.gif"))
        self.__images.append(tk.PhotoImage(file=__file__[0:-8]+"media/img/bonhomme6.gif"))
        self.__images.append(tk.PhotoImage(file=__file__[0:-8]+"media/img/bonhomme7.gif"))
        self.__images.append(tk.PhotoImage(file=__file__[0:-8]+"media/img/bonhomme8.gif"))
        self.__nb_vie = 7


    def lance_jeu(self, mot):
        print(mot)
        if len(mot.replace(" ", "")) == 0:
            self.lance_jeu_rnd()
        else:
            self.__frame_start.destroy()
            self.__frame_jeu.grid()
            self.__mot_mystere = mot
            self.__maj()


    def lance_jeu_rnd(self):
        self.__frame_start.destroy()
        self.__frame_jeu.grid()
        self.__mot_mystere = rnd.choice(self.__liste_mot)[:-1]
        self.__maj()


    def verif_mot(self, mot):
        print(self.__mot_mystere)
        print(mot)
        if len(mot) > 1:
            if mot == self.__mot_mystere:
                self.gagner()
            else:
                self.__nb_vie -= 1
        else:
            if mot in self.__mot_mystere:
                self.__lettre_dite.append(mot)
            else:
                self.__nb_vie -= 1
        if self.__nb_vie == 0:
            self.perdu()
        else:
            self.__maj()

    def set_canvas(self, can):
        self.__canvas = can
        self.__canvas.create_image(150, 150, image = self.__images[0])

    def set_mot(self, mot):
        self.__label_mot = mot

    def set_vie(self, vie):
        self.__label_vie = vie

    def __maj(self):
        self.__label_mot.config(text = self.__cache_mot())
        self.__label_vie.config(text = str(self.__nb_vie))
        self.__canvas.create_image(150, 150, image = self.__images[7 - self.__nb_vie])

    def __cache_mot(self):
        tmp = ""
        for val in self.__mot_mystere:
            if val in self.__lettre_dite:
                tmp = tmp[:]+val
            else:
                tmp = tmp[:]+"_ "
        return tmp

    def gagner(self):
        self.__frame_jeu.destroy()
        self.__frame_gagner.grid()

    def perdu(self):
        self.__frame_jeu.destroy()
        self.__frame_perdu.grid()