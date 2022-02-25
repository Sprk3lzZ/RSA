from ZEGHICHE_WIART_RSA_PA import *


def prim(n):
    """
    Fonction qui renvoie si un nombre est premier en utilisant le critère de primatlité.
    :param n: Integer
    :return: Boolean
    """
    prem = True

    for i in range(2, n):
        if n % i == 0:
            prem = False
    return prem


def Fermat(n, Base):
    """
    Fonction qui renvoie si un nombre est premier en utilisant le théorème de Fermat.
    :param n: Integer
    :param Base: List
    :return: Boolean
    """
    exp = None
    for loop in range(len(Base)):
        for i in range(Base[loop]):
            if exp_mod(Base[loop], n - 1, n) != 1:
                return False
            else:
                exp = exp and True
    return exp


def nb_euler(n):
    """
    Fonction qui calcule et renvoie la liste des n premiers nombres d'Euler.
    :param n: Integer
    :return: List
    """

    list = []

    for loop in range(n):
        list.append(loop ** 2 + loop + 41)
    return list


def pseudo_premiers(euler):
    """
    Fonction qui construie et renvoie une liste de nombres pseudos premier.
    :param euler: List ( list de nombre d'euler  )
    :return: List ( pseudos premiers )
    """

    list = []

    for loop in euler:
        if prim(loop):
            list.append(loop)
    return list


print(prim(5))
print(prim(11))
print(prim(17))
print(prim(21))

print()

Fermat(23, [2, 3, 5, 7])
Fermat(21, [2, 3, 5, 7])

print(nb_euler(107))

print(pseudo_premiers(nb_euler(107)))
