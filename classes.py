#! /usr/bin/env python3

""" Exemple de création de classe en python
TODO : Enregistrer les étudiants dans une variable de classe 
Afficher leurs noms et leurs groupes dans la méthode de classe afficher_resume
"""


class Etudiant:
    nombre_etudiants = 0  # Variable de classe

    # Méthode de classe : travaille sur les données communes à toute la classe (cls.nombre_etudiants).
    # L'appel instance.foo() transmet automatiquement la classe cls comme premier argument de la méthode 
    @classmethod
    def afficher_resume(cls):
        print(f"étudiants : {cls.nombre_etudiants}")

    # Constructeur : utilisé lors de l'appel à Etudiant()
    def __init__(self, n, g):
        self.nom = n
        self.groupe = g
        Etudiant.nombre_etudiants += 1

    # Méthode d'instance : travaille sur les données d'un objet particulier (self.nom, self.groupe).
    # L'appel instance.foo() transmet automatiquement l'instance self comme premier argument de la méthode
    def afficher(self):
        print(f"{self.nom} est en {self.groupe}, dans le {Etudiant.extraire_groupe_td(self.groupe)}")

    # Méthode statique : n'est destinataire d'aucun paramètre automatique
    # Peut être appelée par le nom de la classe Etudiant.extraire_groupe_td(groupeTP) 
    # ou depuis une instance : e.extraire_groupe_td(groupeTP)
    # Elle permet d'effectuer une opération indépendante de l'objet et de la classe
    @staticmethod
    def extraire_groupe_td(groupe): 
       return "TD " + groupe[0:1] 


def tests():
    e1 = Etudiant("Alice", "A1")
    e2 = Etudiant("Bob", "A2")
    e1.afficher()
    e2.afficher()
    e1.afficher_resume()


if __name__ == "__main__":
    tests()