"""
            +======================+
            |                      |
            |       PARTIE 1       |
            |                      |
            +======================+
"""


def mod(a: int, n: int) ->int:
    """
	Effectue un modulo.
	:param a: Le nombre à "moduler"
	:param n: Le modulo
	:return: Le résultat de l'opération modulaire
	"""
    while a >= n:
        a = a - n
        
    while a < 0 :
        a = a + n
      
    return a 

def add_mod(a: int, b: int, n: int) ->int:
    """
	Effectue une addition modulaire : a + b mod n.
	:param a: Le premier nombre à additioner
	:param b: Le second nombre à additioner
	:param n: Le modulo
	:return: La somme modulaire
	"""
    # TODO
    somme = a + b #Additionner a et b
    return mod(somme, n) #Faire modulo entre l'addition et n


def mul_mod(a: int, b: int, n: int) ->int:
    """
	Effectue une multiplication modulaire : a * b mod n.
	:param a: Le premier nombre à multiplier
	:param b: Le second nombre à multiplier
	:param n: Le modulo
	:return: Le produit modulaire
	"""
    # TODO
    mult = a * b #Multiplier a et b
    return mod(mult, n) #Faire modulo entre la multiplication et n


def shift(a: int, n: int, length: int) ->int:
    """
	Effectue un shift CYCLIQUE de :times positions sur la GAUCHE d'un nombre :a, modulo n
	:param a: Le nombre à décaler
	:param n: Le nombres de fois qu'il faut décaler le nombre a.
	:param length: Le nombre maximum de bits toléré avant de cycler. Par exemple, 4 bits permettra d'obtenir tous
					les nombres dans [0-15] (compris), mais pas 16 (qui est sur 5 bits: 10000)
	:return: Le nombre décalé
	:NOTE: La fonction shift est cyclique.
	"""
    # TODO
    pass


def xor(a: int, b: int) ->int:
    """
	Effectue une opération XOR (ou exclusif) sur deux nombres, bit par bit.
	Par exemple : 64 et 65 donneront 1.
	Pour rappel: XOR est positif si exactement l'un des deux éléments est vrai.
	:param a: Le premier nombre à XOR
	:param b: Le second nombre à XOR
	:return: Le XOR des deux nombres
	"""
    # TODO
    return (a | b) & ~(a & b) #XOR = (a OU b) ET NON (a ET b)


"""
            +======================+
            |       PARTIE 2       |
            |  À faire pendant le  |
			|   TP2 uniquement !   |
            +======================+
"""


def gcd(a: int, b: int) ->int:
    """
	Retourne le PGCD de deux nombres.
	:param a: Le premier nombre
	:param b: Le second nombre
	:return: Le PGCD des deux nombres
	"""
    # TODO
    pass


def extended_euclide(a: int, b: int) ->(int, int):
    """
	Effectue Euclide Etendu sur deux nombres, a et b.
	Cela permet de trouver les coefficients de Bézout de deux nombres.
	:param a: Le premier nombre
	:param b: Le second nombre
	:return: Les coefficients de Bézout des deux nombres
	"""
    # TODO
    pass


def inv_mod(a: int, n: int) ->int:
    """
	Obtient l'inverse modulaire de :a modulo :n
	:param a: Le nombre sur lequel il faut faire l'inverse modulaire
	:param n: Le modulo sur lequel on travaille
	:return: L'inverse modulaire.
	NOTE : Vous devrez gérer le cas où l'inverse modulaire n'existe pas.
	SI L'INVERSE MODULAIRE N'EXISTE PAS, VOUS DEVREZ RETOURNER 0, et gérer
	ce cas dans votre code.
	"""
    # TODO
    pass


"""
            +======================+
            |       PARTIE 3       |
            |  À faire pendant le  |
			|   TP3 uniquement !   |
            +======================+
"""


def exp_mod(a: int, b: int, n: int) ->int:
    """
	Calcule l'exponentiation modulaire de a^b mod m.
	:param a: La base
	:param b: L'exposant
	:param n: Le modulo
	:return: Le résultat
	"""
    # TODO
    pass


def is_prime(a: int) ->bool:
    """
	Vérifie que le nombre :n est premier ou non
	:param a: Le nombre à vérifier
	:return: Vrai si le nombre est premier, faux autrement
	"""
    # TODO
    pass


def generate_prime(b: max) ->int:
    """
	Génère un nombre premier entre [2, b] (b inclus).
	:param b: La limite supérieure à respecter lors de la génération
	:return: Un nombre supposément premier.
	"""
    # TODO
    pass


def is_generator(a: int, n: int) ->bool:
    """
	Vérifie si un nombre :a est générateur du groupe Zn*.
	:param a: Le nombre à vérifier
	:param n: Le groupe dans lequel on vérifie :a
	:return: Vrai si le nombre est générateur, faux autrement.
	"""
    # TODO
    pass


def find_all_generators(n: int) ->list:
    """
	Génère la liste de tous les générateurs du groupe Zn*
	:param n: Le groupe dans lequel on veut obtenir tous les générateurs.
	:return: La liste de tous les générateurs
	"""
    # TODO
    pass
