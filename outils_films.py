def compter(liste):
    compter = 0
    for nombre in liste:
        compter = compter + 1
    return compter


def plus_long_titre(liste):
    plus_long = liste[0]
    for titre in liste:
        if len(titre) > len(plus_long):
            plus_long = titre
    return plus_long


def titres_courts(liste,limite):
    court = []
    for titre in liste:
        if len(titre) < limite:
            court.append(titre)
    return court








