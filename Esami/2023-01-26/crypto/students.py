import base64
import string

ALPHABET = list(string.printable)  
LEN = len(ALPHABET)

with open('encrypted_flag.txt', 'r') as f:
    encrypted_message=f.read()

def reverse_base64_decode(text):
    # Aggiungi il padding mancante
    padding_length = (4 - len(text) % 4) % 4
    text += '=' * padding_length

    decoded_bytes = base64.b64decode(text)
    return decoded_bytes.decode('utf-8')

def ROTdecode(message, pos):
    rot13_enc = ''
    for c in message:
        i = ALPHABET.index(c)
        rot13_enc += ALPHABET[(i - pos)%LEN]
    return rot13_enc

print(reverse_base64_decode(ROTdecode(encrypted_message, 13)))