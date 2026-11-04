#! /usr/bin/env python3

"""Listes simplement chaînées

TODO : 
Produire une version récursive de la fonction d’affichage 
Produire des fonctions calculant la taille de la liste en versions itératives et récursives
Tester pour des listes de taille vide, réduite à un élément ou plus longues
[BONUS] Permettre de pouvoir donner un nom à une liste
[BONUS] Ajouter un compteur permettant de savoir le nombre total de cellules produites pour gérer toutes les listes construites
"""

class Cellule:

    @classmethod
    def afficher_nombre_cellules_creees(cls):
        print("Nb de cellules créees : " + str(cls.nombre_cellules_creees))

    def __init__(self, val, suiv=None):
        self.valeur = val   
        self.suivant = suiv

class ListeChainee:
    def __init__(self, n=None):
        self.tete = None

    def est_vide(self):
        return self.tete is None

    def cellule_tete(self):
        return self.tete

    def inserer_tete(self, val):
        nouvelle = Cellule(val, self.tete) 
        self.tete = nouvelle

    def supprimer_tete(self):      
        if self.tete is not None: 
            seconde = self.tete.suivant
            self.tete = seconde

    def afficher(self):
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

    # Nombre de cellules en version itérative
    def longueur(self):
        return 0

    # Nombre de cellules en version récursive
    # utilisation d'une fonction locale
    def longueur_recursif(self):
        def longueur_rec(cell): 
            # A compléter : fonction locale
            # ordre de la récurrence ?
            # cas de base ? 
            # cas général ?
            return 0 
                
        if self.tete is None: 
            return 0
        else :
            return longueur_rec(self.tete)   


    def inserer_queue(self, val):
        if self.tete is None:
            self.tete = Cellule(val)
        else:
            courant = self.tete
            while courant.suivant is not None:   # on s'arrête sur la dernière cellule
                courant = courant.suivant
            courant.suivant = Cellule(val)

    def inserer_queue_recursif(self, val):
        def inserer_aux(cell):
            # précondition : cell n'est pas None
            # cas de base : cell est la dernière cellule, on y accroche la nouvelle
            # cas général : on insère dans la suite de la liste
            if cell.suivant is None:
                cell.suivant = Cellule(val)
            else:
                inserer_aux(cell.suivant)
 
        if self.tete is None:
            self.tete = Cellule(val)
        else:
            inserer_aux(self.tete)


    def supprimer_queue(self):      
        if self.tete is None:
            return
        if self.tete.suivant is None:            # un seul élément : la liste devient vide
            self.tete = None
        else:
            courant = self.tete
            while courant.suivant.suivant is not None:   # on s'arrête sur l'avant-dernière cellule
                courant = courant.suivant
            courant.suivant = None
    
    def supprimer_queue_recursif(self):
        def supprimer_aux(cell):
            # précondition : cell n'est pas None et cell.suivant n'est pas None
            # cas de base : cell est l'avant-dernière cellule, on détache la dernière
            # cas général : on supprime la queue dans la suite de la liste
            if cell.suivant.suivant is None:
                cell.suivant = None
            else:
                supprimer_aux(cell.suivant)
 
        if self.tete is None:
            return
        if self.tete.suivant is None:
            self.tete = None
        else:
            supprimer_aux(self.tete)



def tests():
    """"""
    L = ListeChainee()
    L.inserer_tete(10)
    L.inserer_tete(20)
    L.inserer_tete(30)

    L1 = ListeChainee()
    L1.inserer_tete(1)
    
    L2 = ListeChainee()

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

    L.supprimer_queue_recursif(); L.afficher()
    L.supprimer_queue_recursif(); L.afficher()
    L.supprimer_queue_recursif(); L.afficher()
    L.supprimer_queue_recursif(); L.afficher()

    L.inserer_queue_recursif(1); L.afficher()
    L.inserer_queue_recursif(2); L.afficher()
    L.inserer_queue_recursif(3); L.afficher()

    verifications()

def valeurs(liste):
    """Contenu d'une liste sous forme de liste python (pour les vérifications)."""
    res = []
    courant = liste.tete
    while courant is not None:
        res.append(courant.valeur)
        courant = courant.suivant
    return res
 
 
def verifications():
    """Vérifications automatiques : listes vide, à un élément, plus longues ; itératif = récursif."""
    for contenu in ([], [1], [1, 2], [1, 2, 3, 4, 5]):
        L = ListeChainee()
        for v in reversed(contenu):
            L.inserer_tete(v)
        assert valeurs(L) == contenu
        assert L.longueur() == L.longueur_recursif() == len(contenu)
 
        for ins in (ListeChainee.inserer_queue, ListeChainee.inserer_queue_recursif):
            M = ListeChainee()
            for v in reversed(contenu):
                M.inserer_tete(v)
            ins(M, 99)
            assert valeurs(M) == contenu + [99]
            assert M.longueur() == len(contenu) + 1
 
        for sup in (ListeChainee.supprimer_queue, ListeChainee.supprimer_queue_recursif):
            M = ListeChainee()
            for v in reversed(contenu):
                M.inserer_tete(v)
            sup(M)
            assert valeurs(M) == contenu[:-1]
 
    # [BONUS] nom de liste et compteur de cellules
    avant = Cellule.nombre_cellules_creees
    N = ListeChainee("ma liste")
    N.inserer_tete(1); N.inserer_queue(2); N.inserer_queue_recursif(3)
    assert Cellule.nombre_cellules_creees == avant + 3
    N.afficher(); N.afficher_recursif()
    ListeChainee("vide").afficher_recursif()
    Cellule.afficher_nombre_cellules_creees()
    print("Toutes les vérifications sont passées.")

if __name__ == "__main__":
    tests()
