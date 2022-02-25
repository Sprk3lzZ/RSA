from ZEGHICHE_WIART_RSA_PA import *
import random


def pgcd(a, b):
    """
    Fonction qui détermine et renvoie le pgcd des nombres a et b.
    :param a: Integer
    :param b: Integer
    :return: Integer ( Plus Grand Commun Denominateur )
    """

    if b == 0:
        return a
    else:
        r = a % b
        return pgcd(b, r)


def clef_publique(p, q):
    """
    Fonction qui génère et renvoi le couple (N,e) en fonction des nb p et q.
    :param p: Integer ( nombre premier )
    :param q: Integer ( nombre premier )
    :return: Tuple
    """

    N = p * q
    N_2 = (p - 1) * (q - 1)

    while True:
        e = random.randrange(1, N_2)
        if pgcd(e, N_2) == 1:
            return (N, e)


def cryptage(x, clef):
    """
    Fonction qui calcule le nombre y = x^e mod N.
    :param x: Integer ( code à crypter )
    :param clef: Integer ( clef publique )
    :return: Integer ( message crypté )
    """

    N, e = clef

    return exp_mod(x, e, N)


def clef_privee(p, q, e):
    """
    Fonction  qui génère et calcule la clef privée (N, d).
    :param p: Integer ( nombre premier )
    :param q: Integer ( nombre premier )
    :param e:
    :return: Tuple
    """

    N = p * q
    N_2 = (p - 1) * (q - 1)

    while True:
        d = random.randrange(1, N_2)
        if pgcd(e, N_2) == 1:
            return (N, d)


def decryptage(y, clef):
    """
    Fonction qui calcule le nombre y =
    :param y:
    :param clef: Integer ( clef publique )
    :return: Integer ( message crypté )
    """

    N, e = clef

    return exp_mod(y, e, N)






# print(pgcd(20, 30))
# print(clef_publique(7, 11))
# print(cryptage(3, (77, 59)))

print(decryptage(3, clef_publique(7, 11)))

