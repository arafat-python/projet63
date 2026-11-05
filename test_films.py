import outils_films
films = ["Dune", "Alien", "Interstellar", "Rocky", "Avatar", "Inception", "Saw"]

def test_compter():
    assert outils_films.compter(films) == 7


def test_plus_long_titre():
    assert outils_films.plus_long_titre(films) == "Interstellar"


def test_titres_courts():
    assert outils_films.titres_courts(films,6) == ['Dune', 'Alien', 'Rocky', 'Saw']

def test_compter_liste_vide():
    assert outils_films.compter([]) == 0



