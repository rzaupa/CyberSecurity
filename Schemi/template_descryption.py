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

def ROTdecode(message, pos): #rotation decode
    rot13_enc = ''
    for c in message:
        i = ALPHABET.index(c)
        rot13_enc += ALPHABET[(i - pos)%LEN]
    return rot13_enc

def XORencode_CGPT(message, key="Hug0"):
    # Assicuriamoci che la chiave sia della stessa lunghezza del messaggio
    key = key * (len(message) // len(key)) + key[:len(message) % len(key)]

    # Eseguiamo l'operazione XOR carattere per carattere
    result = ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(message, key))

    return result

def stringBinaryToStringText(binary):
    # binary è fatta da elementi bit
    message = ""
    for c in binary:
        decimal_value = int(c, 2)
        character = chr(decimal_value)
        message += character
    return message

def replace_chars(input_string, char_dict):
    result = ""
    for char in input_string:
        result += char_dict.get(char, char)
    return result

print(reverse_base64_decode(ROTdecode(encrypted_message, 13)))