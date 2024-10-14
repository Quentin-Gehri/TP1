from ssi_lib import *


def cesar(message,decalage=3):
    
    encrypted_message = ""

    for char in message:
        if 'A' <= char <= 'Z':  
            original_pos = ord(char) - ord('A')
            
            new_pos = mod(original_pos + decalage, 26)
            
            shifted_char = chr(new_pos + ord('A'))
            encrypted_message += shifted_char
        else:
            encrypted_message += char  
    return encrypted_message



def advanced_cesar(message,decalage):
    return cesar(message,decalage)



cesar("HELLO")