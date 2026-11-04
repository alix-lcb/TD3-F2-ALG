#! /usr/bin/env python3

"""Implémentation des files à l'aide de listes python """


class File:

    def __init__(self): 
        pass

    def est_vide(self): 
        pass

    def premier(self) : 
        pass
    
    def enfiler(self, x): 
        pass
    
    def defiler(self):
        pass
    
    def longueur(self): 
        pass
    
    def afficher(self):
        pass


if __name__ == "__main__":
    p1 = File() 
    p1.enfiler(1)
    p1.enfiler(2)
    p1.enfiler(3)
    p1.afficher()
    
    v = p1.defiler(); print("Extrait : " + str(v))
    v = p1.defiler(); print("Extrait : " + str(v))
    v = p1.defiler(); print("Extrait : " + str(v))
    p1.afficher()
    
