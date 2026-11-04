#! /usr/bin/env python3

"""Listes doublement chaînées"""

class CelluleDoublementChainee:

    def __init__(self, val, suiv=None):
        self.valeur = val   
        self.suivant = suiv
        self.precedent = None
        if suiv is not None:
            suiv.precedent = self

class ListeDoublementChainee:
    def __init__(self):
        self.tete = None
        self.queue = None

    def est_vide(self):
        return self.tete is None

    def cellule_tete(self):
        return self.tete

    def cellule_queue(self):
        return self.queue

    # Ajouter en début sans oublier le double chainage et le pointeur de queue
    def inserer_tete(self, val):
        pass

    def supprimer_tete(self):      
        pass

    def inserer_queue(self, val):
        pass
 
    def supprimer_queue(self):      
        pass
    
     # Nombre de cellules en version itérative
    def longueur(self):
        return 0

    # Nombre de cellules en version récursive
    def longueur_recursif(self):
        return 0 
        
    def afficher(self):
        if self.tete is not None: 
            print("Valeur en tete : " + str(self.tete.valeur))
        else :
            print("Tete is None")

        if self.queue is not None: 
            print("Valeur en queue : " + str(self.queue.valeur))
        else :
            print("Queue is None") 

        if self.tete is None: 
            print("Liste vide !")

        courant = self.tete
        while courant is not None:
            print(courant.valeur, end=" -> ")
            courant = courant.suivant
        print("None")

    def afficher_recursif(self):
        def afficher_aux(cell) : 
            # A compléter : fonction locale
            # ordre de la récurrence ?
            # cas de base ? 
            # cas général ?
            pass

        if self.tete is None: 
            print("Liste vide !")
        else:
            afficher_aux(self.tete)

def tests():
    """"""
    L = ListeDoublementChainee()
    L.inserer_tete(10)
    L.inserer_tete(20)
    L.inserer_tete(30)

    L1 = ListeDoublementChainee()
    L1.inserer_tete(1)
    
    L2 = ListeDoublementChainee()

    L.afficher()
    L1.afficher()
    L2.afficher()

    L.afficher_recursif()
    L1.afficher_recursif()
    L2.afficher_recursif()

    print(L.longueur())
    print(L1.longueur())
    print(L2.longueur())

    print(L.longueur_recursif())
    print(L1.longueur_recursif())
    print(L2.longueur_recursif())

    L.supprimer_tete(); L.afficher()
    L.supprimer_tete(); L.afficher()
    L.supprimer_tete(); L.afficher()
    L.supprimer_tete(); L.afficher()

    L.inserer_tete(1); L.afficher()
    L.inserer_tete(2); L.afficher()
    L.inserer_tete(3); L.afficher()
    
    # BONUS
    L.supprimer_queue(); L.afficher()
    L.supprimer_queue(); L.afficher()
    L.supprimer_queue(); L.afficher()
    L.supprimer_queue(); L.afficher()

    L.inserer_queue(1); L.afficher()
    L.inserer_queue(2); L.afficher()
    L.inserer_queue(3); L.afficher()

if __name__ == "__main__":
    tests()