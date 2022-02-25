from ZEGHICHE_WIART_RSA_PC import *


def message(a):
    """
    Fonction qui permet de crypter et décrypter une phrase déjà découpée en blocs de trois caractères avec le code RSA.
    :param a: String
    :return: String
    """
    a = [a[i:i+3] for i in range(0, len(a), 3)]
    for i in range(len(a)):
        t = ""
        for e in range(len(a[i])):
            t = t + str(ord(a[i][e]))
            while not len(t) % 3 == 0:
                t = '0' + t
        while len(t) < 9:
            t += '0'
        a[i] = t
    print(a)
    b = []
    clef_p = (37687171,12689281)
    clef_pr = (37687171,18267121)
    for i in a:
        for e in range(0,9,1):
            b.append(cryptage(int(i[e]), clef_p))
    print(b)
    c = ""
    for i in range(0,len(b),3):
        c += chr(int(str(decryptage(b[i],clef_pr)) + str(decryptage(b[i+1],clef_pr)) + str(decryptage(b[i+2],clef_pr))))
    print(c)

a = "Bonjour"

for i in a:
    print(ord(i))

message(a)
