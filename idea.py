import argparse

from ssi_lib import shift, mul_mod, add_mod, xor, inv_mod, mod
def replace_zero(val):
	if val == 16 :
		return 0
	elif val == 0:
		return 16
	else:
		return val
	

def mul_mod_idea(a,b,n):
	return replace_zero(mul_mod(replace_zero(a),replace_zero(b),n))


def full_round(message_blocks: list, subkeys: list) -> list:
		
		"""
		Effectue un round complet de l'algorithme IDEA.
		:param message_blocks: Le messages sous forme de bloc (X1, X2, X3, X4)
		:param subkeys: Les sous-clés. Il doit y en avoir EXACTEMENT autant que pour un round 	(soit 6).
		:return: Les blocks message après un round complet.
		"""
		
    
		x1, x2, x3, x4 =  message_blocks
		z1, z2, z3, z4, z5, z6 = subkeys


		s1 = mul_mod_idea(int(x1), int(z1), 17)
		s2 = add_mod(int(x2), int(z2), 16)
		s3 = add_mod(int(x3), int(z3), 16)
		s4 = mul_mod_idea(int(x4), int(z4), 17)

		s5 = xor(s1, s3)
		s6 = xor(s2, s4)
		
		s7 = mul_mod_idea(s5, int(z5) ,17)
		s8 = add_mod(s6, s7, 16)
		s9 = mul_mod_idea(s8, int(z6), 17)
		s10 = add_mod(s7, s9, 16)

		
		final_x1 = xor(s1, s9)
		final_x2 = xor(s3, s9)
		final_x3 = xor(s2, s10)
		final_x4 = xor(s4, s10)
		
		return [final_x1, final_x3,final_x2, final_x4]


def half_round(message_blocks: list, subkeys: list) -> list:
	"""
	Effectue un demi-round d'algorithme IDEA.
	:param message_blocks: Le message sous forme de bloc (X1, X2, X3, X4)
	:param subkeys: Les sous-clés. Il doit y en avoir EXACTEMENT autant que pour un round (soit 6).
	:return: Les blocks message après un demi-round.
	"""
	# TODO
	x1, x2, x3, x4 = message_blocks
	z1, z2, z3, z4 = subkeys
	result = [
		mul_mod_idea(int(x1), int(z1), 17),
		add_mod(int(x2), int(z2), 16),
		add_mod(int(x3), int(z3), 16),
		mul_mod_idea(int(x4), int(z4), 17),
	]
	return result

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
	debut = 0
	fin = 4
	for i in range(0,5):
		subkey = []
		j = 0
		while j < 6:
			subkey.append(int(key[debut:fin], 2))
			if fin > 31:
				key = bin(shift(int(key), 6, 32))[2:]
				while len(key) < 32:
					key = "0" + key
				debut = 0
				fin = 4
			else:
				debut+=4
				fin+=4
			j+=1
			if len(subkeys_list) == 4 and len(subkey) == 4:
				subkeys_list.append(subkey)
				return subkeys_list
		subkeys_list.append(subkey)

def encrypt(message: str, subkeys: list) -> str:
	"""
	Effectue le chiffrement IDEA en fonction d'un message et d'une liste de sous-clés.
	:param message: Un message faisant EXACTEMENT 16 bits (2 caractères)
	:param subkeys: Les 28 sous-clés.
	:return: Le message chiffré.
	"""
	# TODO
	liste_message = []
	chaine = ""
	for i in range(0, len(message), 4):
		liste_message.append(message[i:i + 4])
	for i in range(0,len(subkeys)-1,1):
		liste_message = full_round(liste_message, subkeys[i])
	res = half_round(liste_message, subkeys[-1])
	for element in res:
		chaine+=str(bin(element)[2:])
	return chaine

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
	return message + "00100000"

def group(message: str) -> list:
	"""
	Cette méthode doit créer des blocs pour que le message puisse être "digéré" par votre algorithme de chiffrement.
	:param message: Le message à chiffrer
	:return: Une liste de blocs qui sera passée à votre algo de chiffrement, bloc par bloc.
	"""
	# TODO
	l = []
	for i in range(0,len(message),16):
		l.append(message[i:i+16])
	return l

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