# region PARTIE A
import random


def exp_base(a, n, p):
    """
    Fonction qui calcule et renvoie les puissances successives de a puis le modulo p de a^n.
    :param a: Integer
    :param n: Integer ( exposant )
    :param p: Integer ( modulo )
    :return: Integer
    """
    result = 1

    for loop in range(n):
        result = (result * a) % p
    return result


def exp_mod(a, n, p):
    """
    Fonction qui calcule et renvoie l'éxponentiation modulaire.
    :param a: Integer
    :param n: Integer ( exposant )
    :param p: Integer ( modulo )
    :return: Integer
    """

    x = a
    y = 1

    while n > 0:
        if n % 2 != 0:
            y = (y * x) % p
            n -= 1
        else:
            x = (x * x) % p
            n /= 2
    return y


def lpowmod(x, y, n):
    """
    Fonction qui calcule et renvoie la puissance modulaire: (x**y)%n avec x, y et n entiers.
    :param x: Integer
    :param y: Integer ( exposant )
    :param n: Integer ( modulo )
    :return: Integer
    """

    result = 1

    while y > 0:
        if (y & 1) > 0:
            result = (result * x) % n
        y >>= 1
        x = (x * x) % n
    return result


# print(exp_base(3, 12, 11))
# print(exp_base(123456, 654321, 789))
#
# print(exp_mod(3, 12, 11))
# print(exp_mod(123456, 654321, 789))
#
# print(lpowmod(3, 12, 11))
# print(lpowmod(123456, 654321, 789))


# endregion

# region PARTIE B

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
    for loop in range(len(Base)):
        for i in range(Base[loop]):
            if exp_mod(Base[loop], n - 1, n) != 1:
                print('Base', Base[loop], ':', False)
            else:
                print('Base', Base[loop], ':', True)
        print()


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
    Fonction
    :param euler:
    :return:
    """

    list = []

    for loop in euler:
        if prim(loop):
            list.append(loop)
    return list


# print(prim(5))
# print(prim(11))
# print(prim(17))
# print(prim(21))
#
# print()
#
# Fermat(23, [2, 3, 5, 7])
# Fermat(21, [2, 3, 5, 7])

# print(nb_euler(107))
#
# print(pseudo_premiers(nb_euler(107)))
# endregion

def pgcd(a, b):
    """

    :param a:
    :param b:
    :return:
    """

    if b == 0:
        return a
    else:
        r = a % b
        return pgcd(b, r)


def clef_publique(p, q):
    """

    :param p:
    :param q:
    :return:
    """

    N = p * q
    N_2 = (p - 1) * (q - 1)

    while True:
        e = random.randrange(1, N_2)
        if pgcd(e, N_2) == 1:
            break

    return (N, e)


def cryptage(x, clef):
    """

    :param x:
    :param clef:
    :return:
    """
    N, e = clef

    return exp_mod(x, e, N)


print(pgcd(20, 30))
print(clef_publique(7, 11))
print(cryptage(3, (77, 59)))
