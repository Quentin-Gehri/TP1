import argparse, random
import os.path

from ssi_lib import generate_prime, find_all_generators, exp_mod, mul_mod, inv_mod, gcd, mod

def generate_keys() -> (int, int, int, int):
	"""
	Génère une paire de clés (p, g, A) publique et (a) privée.
	:return: La paire de clés d'abord publique puis privée, le tout dans un seul tuple.
	"""
	p = generate_prime(10000)
	liste_g = find_all_generators(p)
	g = liste_g[random.randint(1, len(liste_g)-1)]
	a = random.randint(1, p - 2)
	A = exp_mod(g, a, p)

	return p, g, A, a


def write_keys(a: int, p: int, g: int, A: int) -> None:
	"""
    Ecrit une paire de clés. La clé privée sera nommée key, et la clé publique key.pub.
    Votre fonction écrit sur le disque dur les deux fichiers selon le format spécifié dans l'énoncé.
    ATTENTION : Si les deux fichiers existent, vous devez faire en sorte de ne pas écraser les fichiers existants.
    :param a: Le nombre entier (clé privée)
    :param p: Le nombre premier
    :param g: Le nombre générateur tq 0 <= a <= p - 1
    :param A: Le calcul des nombres (expmod) avec p, g et a.
    """
	if os.path.exists('key'):
		print("Erreur : Le fichier 'key' existe déjà. Veuillez choisir un autre nom ou supprimer le fichier existant.")
		return
	if os.path.exists('key.pub'):
		print(
			"Erreur : Le fichier 'key.pub' existe déjà. Veuillez choisir un autre nom ou supprimer le fichier existant.")
		return
	with open('key', 'w') as private_file:
		private_file.write(str(a))
	with open('key.pub', 'w') as public_file:
		public_file.write(f" {p}\n {g}\n {A}")

	print("Les clés ont été sauvegardées avec succès.")


def load_keys() -> (int, int, int, int):
    """
    Charge les clés key.pub et key en mémoire.
    :return: Un tuple, contenant d'abord la clé publique (en trois morceaux), puis la privée.
    """
    if not os.path.exists('key') or not os.path.exists('key.pub'):
        print("Erreur : Les fichiers 'key' et 'key.pub' doivent exister.")
        return None
    with open('key', 'r') as private_file:
        a = int(private_file.read().strip())
    with open('key.pub', 'r') as public_file:
        p, g, A = [int(line.strip()) for line in public_file.readlines()]

    return (p, g, A, a)


def sign(message: int, p: int, a: int, g: int) -> (int, int):
	"""
    Effectue la signature El Gamal en fonction du message et de la clé privée du signataire.
    :param message: Le message
    :param p: Le nombre premier
    :param a: La clé privée
    :param g: Le nombre générateur
    :return: Le message signé, suivi des variables Y et S.
    """
	while True:
		k = random.randint(1, p - 2)
		if gcd(k, p - 1) == 1:
			break
	Y = exp_mod(g, k, p)
	h_m = message
	k_inv = inv_mod(k, p - 1)
	S = mod(k_inv * (h_m - a * Y), (p - 1))

	return Y, S


def verify(message: int, A: int, Y: int, S: int, g: int, p: int) -> bool:
	"""
    Vérifie qu'un message soit bien signé par son correspondant.
    :param message: Le message à vérifier (en tant qu'entier).
    :param A: La clé publique.
    :param Y: La composante y de la signature El Gamal.
    :param S: La composante S de la signature El Gamal.
    :param g: Le générateur.
    :param p: Le nombre premier.
    :return: Vrai si le message est signé correctement, Faux autrement.
    """
	V1 = exp_mod(g, message, p)
	V2 = (exp_mod(A, Y, p) * exp_mod(Y, S, p)) % p
	if V1 == V2:
		return True
	else:
		return False


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("mode", help="Le mode d'El Gamal. 0 pour signer, 1 pour vérifier.")
	# Note : on considère que le message à signer est dans le fichier message.txt, et que le message signé sera dans
	#        message_signed.txt
	# Note : c'est à vous de déterminer quelle clé vous devez utiliser (en fonction du mode) !

	args = parser.parse_args()
	# Feuille de route de votre code :
	# Si key ou key.pub n'existent pas:
	#   * Générer les clés
	# Charger les clés : stocker p, g, A de la clé publique et a de la clé privée dans leurs variables respectives.
	# Si le mode (via args.mode) est "0":
	#   * Lire le message dans message.txt. Voir plus bas (1).
	#   * Transformer le message en hash. Voir plus bas (2).
	#   * Générer Y et S via la fonction sign(...)
	#   * Écrire ligne par ligne ("\n" permet de faire une nouvelle ligne vide) dans message_signed.txt :
	#       * Le message
	#       * Y (vous devrez convertir Y en chaîne de caractères via str(Y))
	#       * S (vous devrez convertir S en chaîne de caractères via str(S))
	# Si le mode (via args.mode) est "1":
	#   * Charger le fichier message_signed.txt (cette fois pas en mode binaire), et stocker chaque ligne dans sa
	#     variable correspondante.
	#       * Les premières lignes est le message qui a été signé.
	#       * L'avant-dernière ligne est le premier paramètre de la signature, Y
	#       * La dernière ligne est le second paramètre de la signature, S
	#       * NOTE : Votre fichier _signed.txt peut faire un nombre arbitraire de lignes (min. 3), par exemple dans le
	#                cas où votre message fait plusieurs lignes. Pour retrouver Y et S, vous devez compter à l'envers.
	#                Voir plus bas (3).
	#   * Vérifier la validité de la signature avec verify(...).
	#   * Si votre verify(...) retourne vrai (True) :
	#       * Imprimer dans le terminal "Signature valide."
	#   * Sinon:
	#       * Imprimer dans le terminal "Signature invalide."

	# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

	# (1) - Comment charger un fichier. Vous devez charger le fichier en binaire, ce que nous proposons ici.
	# Notez ici que la fonction open prend deux paramètres : le nom du fichier et son mode. Le rb permet de faire
	# du READ en BINAIRE (read binary : rb).
	# Si vous deviez écrire un fichier, vous feriez open(<votre fichier>, "w").
	with open("message.txt", "r") as msg:
		message = msg.read()
		# (2) - Comment "hasher" un message. Ici, nous convertissons le texte en nombre.
		# NOTE : Ca devrait être une fonction de hachage. Par contre, nous n'avons pas encore vu ce qu'était une
		#        fonction de hachage, nous allons donc utiliser une fonction de substitution "maison" qui permet
		#        de faire raccord. :)
		message_dec = int.from_bytes(message.encode())

	with open("message_signed.txt", "r") as msg:
		message_file = msg.readlines()
		# (3) - Lire la dernière et avant-dernière ligne. Vous pouvez lire un tableau à l'envers en Python.
		# Quand vous faites -1 dans un tableau en Python, cela permet d'accéder au dernier élément du tableau.
		# Le -2 sera l'avant-dernier élément, etc.
		# Vos lignes possèdent un "\n" à la fin, qui correspond au caractère pour faire une ligne en plus.
		# Cela empêche de transformer votre texte en nombre, on peut toutefois utiliser la fonction strip pour
		# effacer ce caractère.
		Y, S = int(message_file[-2].strip()), int(message_file[-1].strip())
		# Note : on peut obtenir toutes les lignes d'un fichier, sauf ses deux dernières, comme ci-dessous.
		# Cela nous retourne un tableau de toutes les lignes du message, ce qui va gêner pour la suite. On peut
		# par contre joindre un tableau avec un "séparateur" avec la méthode join, comme ci-dessous.
		message = "\n".join(message_file[:-2]).strip()

		message_dec = int.from_bytes(message.encode())

	# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
	# Commencez à écrire votre code ici.

if __name__ == '__main__':
	main()