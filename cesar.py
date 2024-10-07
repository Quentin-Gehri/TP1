from ssi_lib import *

ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cesar(dep):
    result = shift(dep,n=2,length=4)
    print(chr(result))
    return ALPHABET[result]


def advanced_cesar():
    pass



cesar("A")