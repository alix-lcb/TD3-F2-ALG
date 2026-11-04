#! /usr/bin/env python3

"""Implémentation des piles à l'aide de listes simplement chainées """

from listes_simplement_chainees import ListeChainee


class Pile:
    
    def __init__(self):
        pass

    def est_vide(self): 
        pass
    
    def sommet(self):
        pass

    def empiler(self, x): 
        pass
    
    def depiler(self):
        pass
    
    def longueur(self): 
        pass
    
    def afficher(self):
        pass

if __name__ == "__main__":
    p1 = Pile()
    p1.empiler(1)
    p1.empiler(2)
    p1.empiler(3)
    p1. afficher()
    
    v = p1.depiler(); print("Extrait : " + str(v))
    v = p1.depiler(); print("Extrait : " + str(v))
    v = p1.depiler(); print("Extrait : " + str(v))
    p1. afficher()

