#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:name: Jeu de dames
:date: septembre-novembre 2022
:auteur: Mathilde Henrion
"""
import json

# Plateau
# b pour les pions blancs
# B pour les dames blanches
# n pour les pions noirs 
# N pour les dames noires
# . pour les cases vides

plateau =   [['0','1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], 
            ['1', '.','n','.','n','.','n','.','n','.','n'],
            ['2', 'n','.','n','.','n','.','n','.','n','.'],
            ['3', '.','n','.','n','.','n','.','n','.','n'],
            ['4', 'n','.','n','.','n','.','n','.','n','.'],
            ['5', '.','.','.','.','.','.','.','.','.','.'],
            ['6', '.','.','.','.','.','.','.','.','.','.'],
            ['7', '.','b','.','b','.','b','.','b','.','b'],
            ['8', 'b','.','b','.','b','.','b','.','b','.'],
            ['9', '.','b','.','b','.','b','.','b','.','b'],
            ['10', 'b','.','b','.','b','.','b','.','b','.']]

# --------------FONCTIONS-PRINCIPALES--------------
# Affichage du tableau
def affiche_tableau(tab) :
    """ 
    Affichage du tableau propre sans les crochets et les guillemets

    Args:
        tab (list(list(str))): tableau
    """
    for i in range(0,len(tab)):
        for j in range(0, len(tab[0])):
            print ('{:<3}'.format(tab[i][j]),end="")
        print ()

# Récupérer les données d'une case
def get(x, y, tab):
    """ 
    Récupère les données contenu dans le tableau aux coordonnées fournies
    Les coordonnées sont sous la forme x est la ligne et y est la colonne

    Args:
        x (int): indice de la ligne du tableau
        y (int): indice de la colonne du tableau
        tab (list(list(str))): tableau
    """
    return(tab[x][y])

# Modifier les données d'une case
def set(x, y, tab, nv):
    """ 
    Modifie la valeur d'une case du tableau à partir des coordonnées
    Les coordonnées sont sous la forme x est la ligne et y est la colonne

    Args:
        x (int): indice ligne du tableau
        y (int): indice colonne du tableau
        tab (list(list(str))): tableau
        nv (str): nouvelle valeur de la case du tableau
    """
    tab[x][y]=nv

# Changement des pions en dames
def changement_dame(pions_joueur, lig_arv, col_arv, tab):
    """
    Change les pions qui sont arrivés de l'autre côté du plateau en dame

    Args:
        pions_joueur (list(str)): les pions du joueur
        lig_arv (int): indice de la ligne d'arrivée
        col_arv (int): indice de la colonne d'arrivée
        tab (list(list(str))): tableau
    """
    if pions_joueur == ['b', 'B']:
        if lig_arv == 1 and get(lig_arv, col_arv, tab)=='b':
            set(lig_arv, col_arv, tab, 'B')
    if pions_joueur == ['n', 'N']:
        if lig_arv == 10 and get(lig_arv, col_arv, tab)=='n':
            set(lig_arv, col_arv, tab, 'N')

# Compte le nombre de pions d'une couleur
def comptage(pions_joueur, tab):
    """
    Renvoie le nombre de pion d'une couleur

    Args:
        pions_joueur (list(str)): les pions du joueur
        tab (list(list(str))): tableau

    Returns:
        int: le nombre de pions d'une couleur
    """
    comptage = 0
    for i in range(1, len(tab)):
        for j in range(1, len(tab[i])):
            if tab[i][j] in pions_joueur:
                comptage += 1
    return comptage

# ------------------VÉRIFICATIONS------------------

# Vérification : la case d'arrivée est vide
def is_case_vide(lig_arv, col_arv, tab):
    """ 
    Vérifie que la case d'arrivée est vide
    Args:
        lig_arv (int): indice de la ligne d'arrivée
        col_arv (int): indice de la colonne d'arrivée
        tab (list(list(str))): tableau

    Returns:
        bool : True si la case est vide
    """
    if get(lig_arv, col_arv, tab) == '.':
        return True
    else:
        return False

# Vérification : le pion est de la bonne couleur
def verif_couleur_pion(pions_joueur, lig_dep, col_dep, tab):
    """ 
    Vérifie que le pion de la case de départ est de la même couleur que le joueur qui est en train de jouer

    Args:
        pions_joueur (list(str)): les pions du joueur
        lig_dep (int): indice de la ligne de départ
        col_dep (int): indice de la colonne de départ
        tab (list(list(str))): tableau

    Returns:
        bool : True si le pion est de la bonne couleur
    """
    if get(lig_dep, col_dep, tab) in pions_joueur:
        return True
    return False

# Vérification : le pion que l'on mange est de la couleur adverse
def verif_couleur_prise_pion(pions_joueur, lig_dep, col_dep, lig_arv, col_arv, tab):
    """ 
    Vérifie que le pion que l'on mange est bien de la couleur adverse

    Args:
        pions_joueur (list(str)): les pions du joueur
        lig_dep (int): indice de la ligne de départ
        col_dep (int): indice de la colonne de départ
        lig_arv (int): indice de la ligne d'arrivée
        col_arv (int): indice de la colonne d'arrivée
        tab (list(list(str))): tableau

    Returns:
        bool : True si le pion à prendre est de la couleur adverse
    """
    if pions_joueur == ['b', 'B']:
            advers = ['n', 'N']
    else:
        advers = ['b', 'B']
    # Quand prise HD
    if lig_arv-lig_dep == -2 and col_arv-col_dep == 2:
        if get(lig_dep-1, col_dep+1, tab) in advers:
            return True
    # Quand prise BD
    if lig_arv-lig_dep == 2 and col_arv-col_dep == 2:
        if get(lig_dep+1, col_dep+1, tab) in advers:
            return True
    # Quand prise BG
    if lig_arv-lig_dep == 2 and col_arv-col_dep == -2:
        if get(lig_dep+1, col_dep-1, tab) in advers:
            return True
    # Quand prise HG
    if lig_arv-lig_dep == -2 and col_arv-col_dep == -2:
        if get(lig_dep-1, col_dep-1, tab) in advers:
            return True
    else:
        return False

# -- DÉPLACEMENTS POUR PRENDRE UN PION --

# Vérification : le déplacement d'un pion est pour prendre un pion (diagonales de 2 cases)
def verif_dep_prise_pion(lig_dep, col_dep, lig_arv, col_arv):
    """ 
    Vérifie que le déplacement est de deux cases en diagonales, pour prendre un pion

    Args:
        lig_dep (int): indice de la ligne de départ
        col_dep (int): indice de la colonne de départ
        lig_arv (int): indice de la ligne d'arrivée
        col_arv (int): indice de la colonne d'arrivée

    Returns:
        bool : True si le déplacement est de deux cases en diagonales
    """
    # Déplacement de prise de pion dans une des quatre diagonales
    if (-2 <= lig_arv-lig_dep < -1 or 1 < lig_arv-lig_dep<= 2) and (-2 <= col_arv-col_dep < -1 or 1 < col_arv-col_dep <=2):
        return True
    else:
        return False

# Vérification : le déplacement d'une dame est pour prendre un pion (diagonale avec un pion)
def verif_dep_dame_avec_prise(pion_joueur, lig_dep, col_dep, lig_arv, col_arv, tab):
    """ 
    Vérifie que le déplacement se fait selon les règles et que la diagonale contient un pion
    
    Args:
        pion_joueur (str): la dame du joueur
        lig_dep (int): indice de la ligne de départ
        col_dep (int): indice de la colonne de départ
        lig_arv (int): indice de la ligne d'arrivée
        col_arv (int): indice de la colonne d'arrivée
        tab (list(list(str))): tableau

    Returns:
        bool: True si la diagonale est vide
    """
    if pion_joueur == 'B':
        advers = ['n','N']
        coul = ['b', 'B']
    elif pion_joueur == 'N':
        advers = ['b', 'B']
        coul = ['n', 'N']
    else:
        return False
    compteur = 0
    prise = False
    coul_pion = True
    if dep_dame_reg:
        # HD
        if (lig_arv-lig_dep < 0) and (col_arv-col_dep > 0):
            i = -1
            j = 1
            while (lig_dep+i >= lig_arv):
                if get(lig_dep+i, col_dep+j, tab) in advers:
                    compteur += 1
                if get(lig_dep+i, col_dep+j, tab) in coul:
                    coul_pion = False    
                i-=1
                j+=1
        # BD
        elif (lig_arv-lig_dep > 0) and (col_arv-col_dep > 0):
            i = 1
            j = 1
            while (lig_dep+i <= lig_arv):
                if get(lig_dep+i, col_dep+j, tab) in advers:
                    compteur += 1
                if get(lig_dep+i, col_dep+j, tab) in coul:
                    coul_pion = False  
                i+=1
                j+=1
        # BG
        elif (lig_arv-lig_dep > 0) and (col_arv-col_dep < 0):
            i = 1
            j = -1
            while (lig_dep+i <= lig_arv):
                if get(lig_dep+i, col_dep+j, tab) in advers:
                    compteur += 1
                if get(lig_dep+i, col_dep+j, tab) in coul:
                    coul_pion = False  
                i+=1
                j-=1
        # HG
        elif (lig_arv-lig_dep < 0) and (col_arv-col_dep < 0):
            i = -1
            j = -1
            while (lig_dep+i >= lig_arv):
                if get(lig_dep+i, col_dep+j, tab) in advers:
                    compteur += 1
                if get(lig_dep+i, col_dep+j, tab) in coul:
                    coul_pion = False  
                i-=1
                j-=1
    if compteur == 1:
        prise = True
    if coul_pion == False:
        prise = False
    return prise

# -- DÉPLACEMENTS RÉGLEMENTAIRES --

# Vérification : le déplacement des pions est réglementaire
def dep_simple_regl(pions_joueur, lig_dep, col_dep, lig_arv, col_arv):
    """ 
    Vérifie que le déplacement respecte les règles soit :
    - les pions se déplace forcément vers l'avant
    - en diagonale
    - d'une seule case

    Args:
        pions_joueur (list(str)): la couleur des pions du joueur
        lig_dep (int): indice de la ligne de départ
        col_dep (int): indice de la colonne de départ
        lig_arv (int): indice de la ligne d'arrivée
        col_arv (int): indice de la colonne d'arrivée

    Returns:
        bool : True si le déplacement respecte les règles
    """
    if pions_joueur == ['b', 'B']: # Déplacement des pions blancs
        # Déplacement que vers l'avant et que en diagonale
        if lig_arv-lig_dep == -1 and -1 <= col_arv-col_dep <= 1  and col_arv-col_dep != 0:
            return True
        else:
            return False
    else: # Déplacement des pions noirs
        # Déplacement que vers l'avant (en bas dans le terminal) et que en diagonale
        if lig_arv-lig_dep == 1 and -1 <= col_arv-col_dep <= 1 and col_arv-col_dep != 0:
            return True
        else:
            return False

# Vérification : le déplacement des dames est réglementaire (diagonale)
def dep_dame_reg(lig_dep, col_dep, lig_arv, col_arv):
    """
    Vérifie que le déplacement des dames est bien en diagonale

    Args:
        lig_dep (int): indice de la ligne de départ
        col_dep (int): indice de la colonne de départ
        lig_arv (int): indice de la ligne d'arrivée
        col_arv (int): indice de la colonne d'arrivée

    Returns:
        bool: True si les déplacement des dames est réglementaire
    """
    reglementaire = False
    if (lig_arv-lig_dep != 0) and (col_arv-lig_arv != 0):
        # Déplacement diagonale HD
        if (lig_arv-lig_dep < 0) and (col_arv-col_dep > 0):
            if (col_arv-col_dep == (lig_arv-lig_dep)+2*(col_arv-col_dep)):
                reglementaire = True
        # Déplacement diagonale BD
        if (lig_arv-lig_dep > 0) and (col_arv-col_dep > 0):
            if (lig_arv-lig_dep) == (col_arv-col_dep):
                reglementaire = True
        # Déplacement diagonale BG
        if (lig_arv-lig_dep > 0) and (col_arv-col_dep < 0):
            if (lig_arv-lig_dep == (col_arv-col_dep)+2*(lig_arv-lig_dep)):
                reglementaire = True
        # Déplacement diagonale HG
        if (lig_arv-lig_dep < 0) and (col_arv-col_dep < 0):
            if (lig_arv-lig_dep) == (col_arv-col_dep):
                reglementaire = True
    return reglementaire

# Vérification : le déplacement des dames sans prise est réglementaie (diagonale vide)
def dep_dame_sans_prise(lig_dep, col_dep, lig_arv, col_arv, tab):
    """ 
    Vérifie que le déplacement se fait selon les règles et que la diagonale ne contient aucun pion
    
    Args:
        lig_dep (int): indice de la ligne de départ
        col_dep (int): indice de la colonne de départ
        lig_arv (int): indice de la ligne d'arrivée
        col_arv (int): indice de la colonne d'arrivée
        tab (list(list(str))): tableau

    Returns:
        bool: True si la diagonale est vide
    """
    vide = True
    if dep_dame_reg:
        # HD
        if (lig_arv-lig_dep < 0) and (col_arv-col_dep > 0):
            i = -1
            j = 1
            while (lig_dep+i >= lig_arv) and vide == True:
                if get(lig_dep+i, col_dep+j, tab) != '.':
                    vide = False
                i-=1
                j+=1
        # BD
        elif (lig_arv-lig_dep > 0) and (col_arv-col_dep > 0):
            i = 1
            j = 1
            while (lig_dep+i <= lig_arv) and vide == True:
                if get(lig_dep+i, col_dep+j, tab) != '.':
                    vide = False
                i+=1
                j+=1
        # BG
        elif (lig_arv-lig_dep > 0) and (col_arv-col_dep < 0):
            i = 1
            j = -1
            while (lig_dep+i <= lig_arv) and vide == True:
                if get(lig_dep+i, col_dep+j, tab) != '.':
                    vide = False
                i+=1
                j-=1
        # HG
        elif (lig_arv-lig_dep < 0) and (col_arv-col_dep < 0):
            i = -1
            j = -1
            while (lig_dep+i >= lig_arv) and vide == True:
                if get(lig_dep+i, col_dep+j, tab) != '.':
                    vide = False
                i-=1
                j-=1
    return vide

# -- DÉPLACEMENTS POSSIBLES -- 

# Vérification : le déplacement simple (1 case en diagonale) est possible
def dep_possible_pion(pions_joueur, tab):
    """
    Vérifie qu'un pion peut se déplacer d'une case en diagonale sur le plateau

    Args:
        pions_joueur (list(str)): les pions du joueur
        tab (list(list(str))): tableau

    Returns:
        bool: True si un pion peut se déplacer
    """
    prise = False
    for i in range(1, len(tab)-1):
        for j in range(1, len(tab)-1):
            if tab[i][j] in pions_joueur:
                if 0<i<9 and 0<j<9:
                    if tab[i+1][j+1] == '.':
                            prise = True
                if 2<i<=10 and 0<j<9:             
                    if tab[i-1][j+1] == '.':
                            prise = True
                if 0<i<9 and 2<j<=10: 
                    if tab[i+1][j-1] == '.':
                            prise = True
                if 2<i<=10 and 2<j<=10: 
                    if tab[i-1][j-1] == '.':
                            prise = True
    return prise

# Vérification : le déplacement d'une dame dans une diagonale vide est possible
def dep_possible_dames(pion_joueur, tab):
    """
    Vérifie qu'une dame peut se déplacer sur le plateau dans une diagonale vide

    Args:
        pion_joueur (str): la dame du joueur
        tab (list(list(str))): tableau

    Returns:
        bool: True si une dame peut se déplacer
    """
    prise = -1
    for i in range(1, len(tab)):
        for j in range(1, len(tab)):
            if tab[i][j] == pion_joueur:
                # BD
                if 0<i<9 and 0<j<9:
                    a = 1
                    b = 1
                    while prise == -1 and a<=9-i and b<=9-j:
                        if tab[i+a][j+b] == '.':
                            prise = 1
                        elif tab[i+a][j+b] != '.':
                            prise = 0
                        a += 1
                        b += 1
                if prise != 1 :
                    prise = -1
                    # HD
                    if 2<i<=10 and 0<j<9:
                        a = -1
                        b = 1
                        while prise == -1 and 0-10-i<=a and b<=9-j:
                            if tab[i+a][j+b] == '.':
                                prise = 1
                            elif tab[i+a][j+b] != '.':
                                prise = 0
                            a -= 1
                            b += 1
                    if prise != 1:
                        prise = -1
                        # BG
                        if 0<i<9 and 2<j<=10:
                            a = 1
                            b = -1
                            while prise == -1 and a<=9-i and 0-10-j<=b:
                                if tab[i+a][j+b] == '.':
                                    prise = 1
                                elif tab[i+a][j+b] != '.':
                                    prise = 0
                                a += 1
                                b -= 1
                        if prise != 1:
                            prise = -1
                            # HG
                            if 2<i<=10 and 2<j<=10:
                                a = -1
                                b = -1
                                while prise == -1 and 0-10-i<=a and 0-10-j<=b:
                                    if tab[i+a][j+b] == '.':
                                        prise = 1
                                    elif tab[i+a][j+b] != '.':
                                        prise = 0
                                    a -= 1
                                    b -= 1
    if prise == 1:
        return True
    return False


# -- PRISES POSSIBLES --

# Vérification : les pions peuvent prendre des pions ou des dames sur le plateau
def prise_possible(pion_joueur, tab):
    """
    Vérifie qu'il y a un pion du joueur qui peut prendre sur le plateau

    Args:
        pion_joueur (str): le pion du joueur (on teste les pions et pas les dames)
        tab (list(list(str))): tableau

    Returns:
        bool: True si un pion peut prendre
    """
    prise = False
    if pion_joueur == 'b':
        advers = ['n', 'N']
    elif pion_joueur == 'n':
        advers = ['b', 'B']
    else:
        return prise
    for i in range(1, len(tab)-1):
        for j in range(1, len(tab)-1):
            if tab[i][j] == pion_joueur:
                if 0<i<9 and 0<j<9:
                    if tab[i+1][j+1] in advers and tab[i+2][j+2] == '.':
                            prise = True
                if 2<i<=10 and 0<j<9:             
                    if tab[i-1][j+1] in advers and tab[i-2][j+2] == '.':
                            prise = True
                if 0<i<9 and 2<j<=10: 
                    if tab[i+1][j-1] in advers and tab[i+2][j-2] == '.':
                            prise = True
                if 2<i<=10 and 2<j<=10: 
                    if tab[i-1][j-1] in advers and tab[i-2][j-2] == '.':
                            prise = True
    return prise

# Vérification : les dames peuvent prendre des pions ou des dames sur le plateau
def prise_possible_dames(pion_joueur, tab):
    """
    Vérifie qu'il y a une dame du joueur qui peut prendre sur le plateau

    Args:
        pion_joueur (str): la dame du joueur (on teste les dames et pas les pions)
        tab (list(list(str))): tableau

    Returns:
        bool: True si une dame peut prendre
    """
    prise = -1
    if pion_joueur == 'B':
        joueur = ['b', 'B']
        advers = ['n', 'N']
    elif pion_joueur == 'N':
        joueur = ['n', 'N']
        advers = ['b', 'B']
    else:
        return False
    for i in range(1, len(tab)):
        for j in range(1, len(tab)):
            if tab[i][j] == pion_joueur:
                # BD
                if 0<i<9 and 0<j<9:
                    a = 1
                    b = 1
                    while prise == -1 and a<=9-i and b<=9-j:
                        if tab[i+a][j+b] in joueur:
                            prise = 0
                        elif tab[i+a][j+b] in advers and tab[i+a+1][j+b+1] == '.':
                            prise = 1
                        elif tab[i+a][j+b] in advers and tab[i+a+1][j+b+1] != '.':
                            prise = 0
                        a += 1
                        b += 1
                if prise != 1 :
                    prise = -1
                    # HD
                    if 2<i<=10 and 0<j<9:
                        a = -1
                        b = 1
                        while prise == -1 and 0-10-i<=a and b<=9-j:
                            if tab[i+a][j+b] in joueur:
                                prise = 0
                            elif tab[i+a][j+b] in advers and tab[i+a-1][j+b+1] == '.':
                                prise = 1
                            elif tab[i+a][j+b] in advers and tab[i+a-1][j+b+1] != '.':
                                prise = 0
                            a -= 1
                            b += 1
                    if prise != 1:
                        prise = -1
                        # BG
                        if 0<i<9 and 2<j<=10:
                            a = 1
                            b = -1
                            while prise == -1 and a<=9-i and 0-10-j<=b:
                                if tab[i+a][j+b] in joueur:
                                    prise = 0
                                elif tab[i+a][j+b] in advers and tab[i+a+1][j+b-1] == '.':
                                    prise = 1
                                elif tab[i+a][j+b] in advers and tab[i+a+1][j+b-1] != '.':
                                    prise = 0
                                a += 1
                                b -= 1
                        if prise != 1:
                            prise = -1
                            # HG
                            if 2<i<=10 and 2<j<=10:
                                a = -1
                                b = -1
                                while prise == -1 and 0-10-i<=a and 0-10-j<=b:
                                    if tab[i+a][j+b] in joueur:
                                        prise = 0
                                    elif tab[i+a][j+b] in advers and tab[i+a-1][j+b-1] == '.':
                                        prise = 1
                                    elif tab[i+a][j+b] in advers and tab[i+a-1][j+b-1] != '.':
                                        prise = 0
                                    a -= 1
                                    b -= 1
    if prise == 1:
        return True
    return False

# Vérification : le pion qui viens d'être déplacé peut remanger
def prise_possible_pion(pion_joueur, lig_dep, col_dep, tab):
    """
    Vérifie que le pion qui viens d'être déplacé peut remanger

    Args:
        pion_joueur (str): le pion du joueur qui viens d'être déplacé
        lig_dep (int): indice de la ligne de départ
        col_dep (int): indice de la colonne de départ
        tab (list(list(int))): tableau

    Returns:
        bool: True si le pion peut remanger
    """
    prise = False
    if pion_joueur == 'b':
        advers = ['n', 'N']
    elif pion_joueur == 'n':
        advers = ['b', 'B']
    else:
        return prise
    if tab[lig_dep][col_dep] == pion_joueur:
        if 0<lig_dep<9 and 0<col_dep<9:
            if tab[lig_dep+1][col_dep+1] in advers and tab[lig_dep+2][col_dep+2] == '.':
                    prise = True
        if 2<lig_dep<=10 and 0<col_dep<9:             
            if tab[lig_dep-1][col_dep+1] in advers and tab[lig_dep-2][col_dep+2] == '.':
                    prise = True
        if 0<lig_dep<9 and 2<col_dep<=10: 
            if tab[lig_dep+1][col_dep-1] in advers and tab[lig_dep+2][col_dep-2] == '.':
                    prise = True
        if 2<lig_dep<=10 and 2<col_dep<=10: 
            if tab[lig_dep-1][col_dep-1] in advers and tab[lig_dep-2][col_dep-2] == '.':
                    prise = True
    return prise

# Vérification : la dame qui vient d'être déplacée peut remanger
def prise_possible_dame(pion_joueur, lig_dep, col_dep, tab):
    """
    Vérifie que la dame qui vient d'être déplacée peut remanger

    Args:
        pion_joueur (str): la dame du joueur qui vient d'être déplacée
        lig_dep (int): indice de la ligne de départ
        col_dep (int): indice de la colonne de départ
        tab (list(list(str))): tableau

    Returns:
        bool: True si la dame peut remanger
    """
    prise = -1
    if pion_joueur == 'B':
        joueur = ['b', 'B']
        advers = ['n', 'N']
    elif pion_joueur == 'N':
        joueur = ['n', 'N']
        advers = ['b', 'B']
    else:
        return False
    # BD
    if 0<lig_dep<9 and 0<col_dep<9:
        a = 1
        b = 1
        while prise == -1 and a<=9-lig_dep and b<=9-col_dep:
            if tab[lig_dep+a][col_dep+b] in joueur:
                prise = 0
            elif tab[lig_dep+a][col_dep+b] in advers and tab[lig_dep+a+1][col_dep+b+1] == '.':
                prise = 1
            elif tab[lig_dep+a][col_dep+b] in advers and tab[lig_dep+a+1][col_dep+b+1] != '.':
                prise = 0
            a += 1
            b += 1
    if prise != 1:
        prise = -1
        # HD
        if 2<lig_dep<=10 and 0<col_dep<9:
            a = -1
            b = 1
            while prise == -1 and 0-10-lig_dep<=a and b<=9-col_dep:
                if tab[lig_dep+a][col_dep+b] in joueur:
                    prise = 0
                elif tab[lig_dep+a][col_dep+b] in advers and tab[lig_dep+a-1][col_dep+b+1] == '.':
                    prise = 1
                elif tab[lig_dep+a][col_dep+b] in advers and tab[lig_dep+a-1][col_dep+b+1] != '.':
                    prise = 0
                a -= 1
                b += 1
        if prise != 1:
            prise = -1
            # BG
            if 0<lig_dep<9 and 2<col_dep<=10:
                a = 1
                b = -1
                while prise == -1 and a<=9-lig_dep and 0-10-col_dep<=b:
                    if tab[lig_dep+a][col_dep+b] in joueur:
                        prise = 0
                    elif tab[lig_dep+a][col_dep+b] in advers and tab[lig_dep+a+1][col_dep+b-1] == '.':
                        prise = 1
                    elif tab[lig_dep+a][col_dep+b] in advers and tab[lig_dep+a+1][col_dep+b-1] != '.':
                        prise = 0
                    a += 1
                    b -= 1
            if prise != 1:
                prise = -1
                # HG
                if 2<lig_dep<=10 and 2<col_dep<=10:
                    a = -1
                    b = -1
                    while prise == -1 and 0-10-lig_dep<=a and 0-10-col_dep<=b:
                        if tab[lig_dep+a][col_dep+b] in joueur:
                            prise = 0
                        elif tab[lig_dep+a][col_dep+b] in advers and tab[lig_dep+a-1][col_dep+b-1] == '.':
                            prise = 1
                        elif tab[lig_dep+a][col_dep+b] in advers and tab[lig_dep+a-1][col_dep+b-1] != '.':
                            prise = 0
                        a -= 1
                        b -= 1
    if prise == 1:
        return True
    return False   


# -------------------DÉPLACEMENTS-------------------

# Déplacement : déplace un pion ou une dame d'une case de départ à une case d'arrivée
def deplacement(pion_joueur, lig_dep, col_dep, lig_arv, col_arv, tab): 
    """ 
    Déplace un pion ou une dame en remplaçant la case de départ par une case vide
    La case de départ est modifiée pour être vide.
    La case d'arrivée est modifiée pour contenir le pion.
    
    Args:
        pion_joueur (str): le pion qui va être déplacé
        lig_dep (int): indice de la ligne de départ
        col_dep (int): indice de la colonne d'arrivée
        lig_arv (int): indice de la ligne d'arrivée
        col_arv (int): indice de la colonne d'arrivée
        tab (list(list(str))): tableau
    """
    set(lig_dep, col_dep, tab, '.')
    set(lig_arv, col_arv, tab, pion_joueur)

# Déplacement : un pion prend un pion ou une dame
def dep_prise_pion(pion_joueur, lig_dep, col_dep, lig_arv, col_arv, tab):
    """ 
    Déplace les pions lors d'une prise.
    La case de départ est modifiée pour être vidée.
    La case d'arrivée est modifiée pour contenir le pion.
    La case où le pion est mangée est modifiée pour être vidée et le pion mangé.

    Args:
        pion_joueur (str): le pion qui se déplace
        lig_dep (int): indice de la ligne de départ
        col_dep (int): indice de la colonne de départ
        lig_arv (int): indice de la ligne d'arrivée
        col_arv (int): indice de la colonne d'arrivée
        tab (list(list(str))): tableau
    """
    # Prise HD
    if lig_arv-lig_dep == -2 and col_arv-col_dep == 2:
        deplacement(pion_joueur, lig_dep, col_dep, lig_arv, col_arv, tab)
        set(lig_dep-1, col_dep+1, tab, '.')
    # Prise BD
    elif lig_arv-lig_dep == 2 and col_arv-col_dep == 2:
        deplacement(pion_joueur, lig_dep, col_dep, lig_arv, col_arv, tab)
        set(lig_dep+1, col_dep+1, tab, '.')
    # Prise BG
    elif lig_arv-lig_dep == 2 and col_arv-col_dep == -2:
        deplacement(pion_joueur, lig_dep, col_dep, lig_arv, col_arv, tab)
        set(lig_dep+1, col_dep-1, tab, '.')
    # Prise HG
    elif lig_arv-lig_dep == -2 and col_arv-col_dep == -2:
        deplacement(pion_joueur, lig_dep, col_dep, lig_arv, col_arv, tab)
        set(lig_dep-1, col_dep-1, tab, '.')

# Déplacement : une dame prend un pion ou une dame
def deplacement_prise_pion(pion_joueur, lig_dep, col_dep, lig_arv, col_arv, tab):
    """ 
    Déplace une dame qui prend un pion.
    La case de départ est modifiée pour être vidée.
    La case d'arrivée est modifiée pour contenir la dame.
    La diagonale est vidée et le pion mangé.
    
    Args:
        pion_joueur (str): la dame du joueur qui se déplace
        lig_dep (int): indice de la ligne de départ
        col_dep (int): indice de la colonne de départ
        lig_arv (int): indice de la ligne d'arrivée
        col_arv (int): indice de la colonne d'arrivée
        tab (list(list(str))): tableau
    """
    if dep_dame_reg:
        # HD
        if (lig_arv-lig_dep < 0) and (col_arv-col_dep > 0):
            i = -1
            j = 1
            while (lig_dep+i >= lig_arv):
                set(lig_dep+i, col_dep+j, tab, '.')
                i-=1
                j+=1
        # BD
        elif (lig_arv-lig_dep > 0) and (col_arv-col_dep > 0):
            i = 1
            j = 1
            while (lig_dep+i <= lig_arv):
                set(lig_dep+i, col_dep+j, tab, '.')
                i+=1
                j+=1
        # BG
        elif (lig_arv-lig_dep > 0) and (col_arv-col_dep < 0):
            i = 1
            j = -1
            while (lig_dep+i <= lig_arv):
                set(lig_dep+i, col_dep+j, tab, '.')
                i+=1
                j-=1
        # HG
        elif (lig_arv-lig_dep < 0) and (col_arv-col_dep < 0):
            i = -1
            j = -1
            while (lig_dep+i >= lig_arv):
                set(lig_dep+i, col_dep+j, tab, '.')
                i-=1
                j-=1
    set(lig_arv, col_arv, tab, pion_joueur)
    set(lig_dep, col_dep, tab, '.')

# --------------------SAUVEGARDE--------------------

# Sauvegarde du plateau
def sauvegarde_plateau(tab):
    """
    Sauvegarde le plateau dans un fichier json

    Args:
        tab (list(list(str))): tableau
    """
    with open("plateau.json","w") as f:
        json.dump(tab, f)

# Sauvegarde du joueur    
def sauvegarde_joueur(joueur):
    """
    Sauvegarde le joueur en cours dans un fichier json

    Args:
        joueur (list(str)): les pions du joueur
    """
    with open("joueur.json","w") as f:
        json.dump(joueur, f)

# Importation du plateau sauvegardé
def importation_plateau():
    """
    Importe les données sauvegardé du plateau de la partie précédente

    Returns:
        list(list(str)): tableau (plateau sauvegardé)
    """
    with open("plateau.json", "r") as f:
        return json.load(f)

# Importation du joueur sauvegardé
def importation_joueur():
    """
    Importe les données sauvegardé du dernier joueur de la partie précédente

    Returns:
        list(str): les pions du joueur (joueur sauvegardé)
    """
    with open("joueur.json", "r") as f:
        return json.load(f)

# -------------------JEU-DE-DAMES-------------------
affiche_tableau(plateau)

def jeu(plateau):
    joueur = ['b', 'B'] # Initialisation du premier joueur comme le joueur blanc
    partie_en_cours=input("Reprendre la dernière partie ? Si oui tapez 'o' : ")
    # Importation du plateau et du joueur de la partie précédente
    if partie_en_cours == 'o':
        plateau = importation_plateau()
        joueur = importation_joueur()
        affiche_tableau(plateau)
    # Réinitilisation du plateau et du joueur de la sauvegarde à un début de partie
    else:
        sauvegarde_plateau(plateau)
        sauvegarde_joueur(joueur)
    # Les joueurs peuvent encore jouer
    while (comptage(['b', 'B'], plateau) > 0 and comptage(('n', 'N'), plateau) > 0) and (dep_possible_pion(joueur, plateau) or dep_possible_dames(joueur[1], plateau) or prise_possible(joueur[0], plateau) or prise_possible_dames(joueur[1], plateau)):
        print("Le joueur est ", joueur)
        # Entrée des coordonnées de départ
        lig_dep = 0
        col_dep = 0
        while not(0 < lig_dep <= 10):
            lig_dep = int(input("Quelle est la ligne de départ du pion ? : "))
        while not(0 < col_dep <= 10):
            col_dep = int(input("Quelle est la colonne de départ du pion ? : "))
        # La case sélectionnée contient un pion de la couleur du joueur
        if verif_couleur_pion(joueur, lig_dep, col_dep, plateau):
            # Ce que contient la case de départ
            pion = get(lig_dep, col_dep, plateau)
            # Entrée des coordonées d'arrivée
            lig_arv = 0
            col_arv = 0
            while not(0 < lig_arv <= 10):
                lig_arv = int(input("Quelle est la ligne d'arrivée du pion ? : "))
            while not(0 < col_arv <= 10):
                col_arv = int(input("Quelle est la colonne d'arrivée du pion ? : "))
            # Test si il y a des pions à prendre sur le plateau par des pions ou des dames
            if prise_possible(pion, plateau) or prise_possible_dames(pion, plateau):
                # Test si le pion sélectionné peut prendre un pion
                if prise_possible_pion(pion, lig_dep, col_dep, plateau) or prise_possible_dame(pion, lig_dep, col_dep, plateau):
                    # PRISES DES PIONS
                    if pion in ('b','n'):
                        # Test si le déplacement est pour prend un pion (diagonale de 2 cases)
                        if verif_dep_prise_pion(lig_dep, col_dep, lig_arv, col_arv):
                            # Test si le pion à manger est de la couleur adverse
                            if verif_couleur_prise_pion(joueur, lig_dep, col_dep, lig_arv, col_arv, plateau):
                                # Toutes les conditions sont remplies : on prend le pion
                                if pion == 'b':
                                    dep_prise_pion('b', lig_dep, col_dep, lig_arv, col_arv, plateau)
                                    changement_dame(joueur, lig_arv, col_arv, plateau)
                                else:
                                    dep_prise_pion('n', lig_dep, col_dep, lig_arv, col_arv, plateau)
                                    changement_dame(joueur, lig_arv, col_arv, plateau)
                                # Test s'il n'y a plus de pion à remanger
                                if prise_possible_pion(pion, lig_arv, col_arv, plateau) == False:
                                    if joueur == ['b', 'B']:
                                        joueur = ['n', 'N']
                                        sauvegarde_joueur(joueur)
                                        sauvegarde_plateau(plateau)
                                    else:
                                        joueur = ['b', 'B']
                                        sauvegarde_joueur(joueur)
                                        sauvegarde_plateau(plateau)
                                # Il y a un pion à remanger
                                else:
                                    print("Tu peux remanger !")
                            # Le pion que le joueur essaie de manger n'est pas de sa couleur ou la case est vide
                            else:
                                print("Ce n'est pas un pion de ta couleur !")
                        # Les coordonnées ne permettent pas de prendre un pion
                        else:
                            print("Tu peux prendre un pion !")
                    # PRISES DES DAMES
                    else:
                        # Test si le déplacement est pour prendre un pion (diagonale de 2 cases)
                        if verif_dep_dame_avec_prise(pion, lig_dep, col_dep, lig_arv, col_arv, plateau):
                            # Toutes les conditions sont remplies : on prend le pion
                            if pion =='B':
                                deplacement_prise_pion('B', lig_dep, col_dep, lig_arv, col_arv, plateau)
                            else:
                                deplacement_prise_pion('N', lig_dep, col_dep, lig_arv, col_arv, plateau)
                            # Test s'il n'y a plus de pion à remanger
                            if prise_possible_dame(pion, lig_arv, col_arv, plateau) == False:
                                    if joueur == ['b', 'B']:
                                        joueur = ['n', 'N']
                                        sauvegarde_joueur(joueur)
                                        sauvegarde_plateau(plateau)
                                    else:
                                        joueur = ['b', 'B']
                                        sauvegarde_joueur(joueur)
                                        sauvegarde_plateau(plateau)
                            # Il y a un pion à remanger
                            else:
                                print("Tu peux remanger !")
                        # Les coordonnées ne permettent pas de prendre un pion
                        else:
                            print("Tu peux prendre un pion !")
                # Le pion sélectionné ne peut pas prendre de pion mais il y a une prise possible
                else:
                    print("Tu peux prendre un pion !")
            # Si il n'y a pas de prises, on vérifie les déplacements simples
            else:
                # DÉPLACEMENTS PIONS
                if pion in ('b','n'):
                    # Test si déplacement simple réglementaire
                    if dep_simple_regl(joueur, lig_dep, col_dep, lig_arv, col_arv) and is_case_vide(lig_arv, col_arv, plateau):
                        # Toutes les conditions sont remplies : on déplace le pion
                        if pion == 'b':
                            deplacement('b', lig_dep, col_dep, lig_arv, col_arv, plateau)
                            changement_dame(joueur, lig_arv, col_arv, plateau)
                        else:
                            deplacement('n', lig_dep, col_dep, lig_arv, col_arv, plateau)
                            changement_dame(joueur, lig_arv, col_arv, plateau)
                        # Fin du tour : changement de joueur
                        if joueur == ['b', 'B']:
                            joueur = ['n', 'N']
                            sauvegarde_joueur(joueur)
                            sauvegarde_plateau(plateau)
                        else:
                            joueur = ['b', 'B']
                            sauvegarde_joueur(joueur)
                            sauvegarde_plateau(plateau)
                    # Le déplacement n'est pas règlementaire
                    else:         
                        print("Ton déplacement n'est pas réglementaire !")
                # DÉPLACEMENTS DAMES
                else:
                    # Test si déplacement simple réglementaire
                    if dep_dame_reg(lig_dep, col_dep, lig_arv, col_arv) and dep_dame_sans_prise(lig_dep, col_dep, lig_arv, col_arv, plateau):
                        # Toutes les conditions sont remplies : on déplace la dame
                        if pion == 'B':
                            deplacement('B', lig_dep, col_dep, lig_arv, col_arv, plateau)
                        else:
                            deplacement('N', lig_dep, col_dep, lig_arv, col_arv, plateau)
                        # Fin du tour : changement de joueur
                        if joueur == ['b', 'B']:
                            joueur = ['n', 'N']
                            sauvegarde_joueur(joueur)
                            sauvegarde_plateau(plateau)
                        else:
                            joueur = ['b', 'B']
                            sauvegarde_joueur(joueur)
                            sauvegarde_plateau(plateau)
                    # Le déplacement n'est pas règlementaire
                    else:         
                        print("Ton déplacement n'est pas réglementaire !")
        # La case sélectionnée est vide ou contient un pion de la couleur de l'adversaire
        else:
            print("Ce n'est pas un pion de ta couleur !")
        # Change les pions qui sont sur les dernières lignes en dames
        changement_dame(joueur, lig_arv, col_arv, plateau)
        sauvegarde_plateau(plateau)
        affiche_tableau(plateau)
    # Le jeu s'arrete car les joueurs ne peuvent plus jouer
    # Raisons de l'arrêt du jeu
    # Plus de pions de la couleur du joueur
    if comptage(['b', 'B'], plateau) == 0:
        print("Le joueur blanc n'as plus de pions")
    elif comptage(['n', 'N'], plateau) == 0:
        print("Le joueur noir n'as plus de pions")
    # Plus de déplacements possibles
    elif not(dep_possible_pion(['b', 'B'], plateau) or dep_possible_dames('B', plateau) or prise_possible('b', plateau) or prise_possible_dames('B', plateau)):
        print("Le joueur blanc ne peut plus bouger")
    elif not(dep_possible_pion(['n', 'N'], plateau) or dep_possible_dames('N', plateau) or prise_possible('n', plateau) or prise_possible_dames('N', plateau)):
        print("Le joueur noir ne peut plus bouger")
    print('Fin de partie')

jeu(plateau)