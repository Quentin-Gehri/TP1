import argparse

from numpy.ma.core import append

from ssi_lib import shift, mul_mod, add_mod, xor, inv_mod, mod


def full_round(message_blocks: list, subkeys: list) -> list:
	"""
	Effectue un round complet de l'algorithme IDEA.
	:param message_blocks: Le messages sous forme de bloc (X1, X2, X3, X4)
	:param subkeys: Les sous-clés. Il doit y en avoir EXACTEMENT autant que pour un round (soit 6).
	:return: Les blocks message après un round complet.
	"""
	# TODO
	pass

def half_round(message_blocks: list, subkeys: list) -> list:
	"""
	Effectue un demi-round d'algorithme IDEA.
	:param message_blocks: Le message sous forme de bloc (X1, X2, X3, X4)
	:param subkeys: Les sous-clés. Il doit y en avoir EXACTEMENT autant que pour un round (soit 6).
	:return: Les blocks message après un demi-round.
	"""
	# TODO
	pass

def generate_subkeys(key: str) -> list:
	"""
	Génère les sous-clés pour l'algo simplifié IDEA.
	:param key: Votre clé doit être 32 bits, soit 4 caractères ASCII.
	:return: La liste de vos sous-clés. Vous devriez en avoir 28.
	:note: ATTENTION : votre tableau doit être en deux dimensions : le tableau principal contient
					   une liste de sous-clés.
					   Exemple : [[sous_clé_round_1_n1, sous_clé_round_1_n2], [sous_clé_round_2_n1, sous_clé_round_2_n2]]
	"""
	# TODO
	subkeys_list = []  # Initialisation d'un tableau vide
	i = 0
	debut = 0
	fin = 4
	while i != 4:
		subkey = []
		j = 0
		while j != 6:
			if fin > 31:
				debut = 0
				fin = 4
				shift(key, 6, 32)
			subkey.append(int(key[debut:fin],2))
			debut+=4
			fin+=4
			j+=1
		subkeys_list.append(subkey)
		i+=1
	return subkeys_list







def encrypt(message: str, subkeys: list) -> str:
	"""
	Effectue le chiffrement IDEA en fonction d'un message et d'une liste de sous-clés.
	:param message: Un message faisant EXACTEMENT 16 bits (2 caractères)
	:param subkeys: Les 28 sous-clés.
	:return: Le message chiffré.
	"""
	# TODO
	pass

def decrypt(cipher: str, subkeys: list) -> str:
	"""
	Effectue le déchiffrement IDEA en fonction d'un message et d'une liste de sous-clés.
	:param cipher: Un cipher faisant EXACTEMENT 16 bits
	:param subkeys: Les 28 sous-clés inverses.
	:return: Le message déchiffré
	"""
	# TODO
	pass

def pad(message: str) -> str:
	"""
	Cette méthode doit ajouter du padding à votre message pour qu'il soit à une taille adaptée à votre algorithme de
	chiffrement.
	:NOTE: Si vous devez faire du padding, faites-le avec un espace vide à votre message.
		   Le binaire pour le caractère espace est 00100000.
	:param message: Le message à pad
	:return: Le message paddé.
	"""
	# TODO
	pass

def group(message: str) -> list:
	"""
	Cette méthode doit créer des blocs pour que le message puisse être "digéré" par votre algorithme de chiffrement.
	:param message: Le message à chiffrer
	:return: Une liste de blocs qui sera passée à votre algo de chiffrement, bloc par bloc.
	"""
	# TODO
	pass

def main():
	# Ne touchez pas à ce code sauf instruction contraire !

	parser = argparse.ArgumentParser()
	parser.add_argument("mode", help="Le mode de chiffrement. 0 pour chiffrer, 1 pour déchiffrer")
	parser.add_argument("message", help="Le message (de 16 bits) que vous souhaitez chiffrer/déchiffrer")
	parser.add_argument("key", help="La clé (de 32 bits) que vous souhaitez utiliser pour le "
	                                "chiffrement/déchiffrement")

	args = parser.parse_args()
	# TODO : changez le code à partir d'ici !
	key = args.key

	pass

if __name__ == '__main__':
	main()