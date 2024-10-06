from ssi_lib import *

ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cesar(dep):
    result = shift(a=ALPHABET.index(dep),n=2,length=3)
     
    return ALPHABET[result]


def advanced_cesar():
    pass