#! /usr/bin/env python3

"""Fichier squelette permettant de fournir des fonctions mais aussi un programme principal pour tester ces fonctions."""

import sys


def foo():
    """Fonction foo qui ne fait rien et ne renvoie rien."""
    #print("Foo speaking...")


if __name__ == "__main__":
    sys.stderr.write("foo(): ")
    print(foo.__doc__, file=sys.stderr)
    print(foo())
