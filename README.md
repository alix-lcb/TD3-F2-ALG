# AAP 2026-2027 -- TD3

## Support de cours

[Support de cours au format Google docs](https://docs.google.com/presentation/d/1mb7qIr4pGOKIhoQuJ-QCe5s-DTDOsZPKee02XI2kdrI/edit?slide=id.h236447f92fc2345c_1_409#slide=id.h236447f92fc2345c_1_409)

## Objectifs du TD 

- Comprendre les structures natives et appréhender leurs usages et leurs performances pour choisir la bonne structure : `list`, `tuples`, `dict/set`. 
- Apprendre à faire des structures auto-référentes, des structures de données complexes
sous forme de classes
- Utiliser des structures linéaires pour résoudre le problème du compte est bon


## Exercice 1 : Classes Python

Le fichier `classes.py` présente une classe simple ̀`Etudiant` qui permet d'illustrer les éléments de syntaxe du python pour la création de classes basiques, ainsi que la différence entre méthode d'instance et méthode de classe.
- La méthode d'instance travaille sur les données d'un objet particulier (`self.nom`, `self.groupe`).
- La méthode de classe travaille sur les données communes à toute la classe (`cls.nombre_etudiants`).
- Le mot-clé `self` désigne l'objet lui-même, tandis que `cls` désigne sa classe.
- Les appels aux méthodes d'instance fournissent implicitement une référence vers l'instance considérée comme premier paramètre.  
    - Lors de l'appel à `e1.foo(params)`, python transmet automatiquement `e1` comme premier argument (`self`) à la fonction `foo`.
    - Un appel à `e1.foo(params)` est équivalent à l'appel à `Etudiant.foo(e1,params)`. 

1. Compléter le fichier `classes.py` pour enregistrer les étudiants dans une variable de classe 
- Afficher leurs noms et leurs groupes dans la méthode de classe `afficher_resume`

## Exercice 2 : Listes simplement chaînées 

Nous utilisons le fichier `listes_simplement_chainees.py` qui décrit une cellule et une liste *simplement chaînée* de cellules. 

2. Produire une version récursive de la fonction d’affichage 
3. Produire des fonctions calculant la taille de la liste en versions itératives et récursives
- Tester pour des listes de taille vide, réduite à un élément ou plus longues
- [BONUS] Permettre de pouvoir donner un nom à une liste
- [BONUS] Ajouter un compteur permettant de savoir le nombre total de cellules produites pour gérer toutes les listes construites

4. [A faire pour préparer le TP4] Implémenter les méthodes des listes simplement chaînées manquantes, en itératif et en récursif. 

## Exercice 3 : Listes doublement chaînées 

Nous utilisons le fichier `listes_doublement_chainees.py` qui décrit une cellule et une liste de cellules *doublement chaînées* : 
- Chaque cellule dispose d'un lien vers la cellule suivante ET vers la cellule précédente
- La structure ListeChainee dispose de liens vers la tête ET la queue de la liste construite  

5. Implémenter les fonctions `inserer_tete` et `inserer_queue` pour les deux types de listes chaînées précédentes
- Comparer l’efficacité de ces fonctions
- [BONUS] Implémenter les fonctions supprimer_tete et  supprimer_queue pour les deux types de listes chaînées précédentes
- [BONUS] Implémenter les fonctions qui le nécessitent de manière récursive

6. [A faire pour préparer le TP4] Implémenter les méthodes des listes doublement chaînées manquantes, en itératif et en récursif. 

## Exercice 4 : Piles

Nous utilisons les fichiers `piles_listes_python.py` et `piles_listes_simplement_chainees.py` pour implémenter le TAD Pile de deux manières.  

7. [A faire pour préparer le TP4] Implémenter le TAD Pile à l'aide de listes simplement chaînées
8. [A faire pour préparer le TP4] Implémenter le TAD Pile à l'aide de listes simplement chaînées

## Exercice 5 : Files

Nous utilisons les fichiers `files_listes_python.py` et `files_listes_doublement_chainees.py` pour implémenter le TAD File de deux manières.  

9. [A faire pour préparer le TP4] Implémenter le TAD File à l'aide de listes doublement chaînées
10. [A faire pour préparer le TP4] Implémenter le TAD File à l'aide de listes doublement chaînées


## Exercice 6 : Notation Polonaise Inverse

Nous utilisons le fichier `evaluation_notation_polonaise_inverse.py` pour implémenter l'évaluation d'expressions arithmétiques utilisant la notation polonaise inverse. Lors de nos évaluations, tous les résultats intermédiaires devront être des entiers *naturels*. Nous considérerons comme invalides les résultats intermédiaires *négatifs* ou *réels*.

11. Implémenter l'évaluation d’une expression NPI fournie comme une liste python
12. Implémenter l'évaluation d’une expression NPI fournie comme une file d’opérandes et d’opérateurs


## Exercice 7 : Résolution du problème du compte est bon

C'est l'objectif du TP4 !
