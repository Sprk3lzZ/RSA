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





