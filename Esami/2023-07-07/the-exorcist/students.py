#!/usr/bin/env python3

import string
import itertools    # if you want, it is not necessary

XOR_KEY='??' # can be only letters

# read the file with the encrypted message
with open('encrypted', 'r') as f:
    encrypted_message=f.read()

def decrypt_message(encrypted_message, key):
    decrypted = []
    key_length = len(key)
    for i, char in enumerate(encrypted_message):
        key_char = key[i % key_length]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        decrypted.append(decrypted_char)
    return ''.join(decrypted)

# Funzione per testare una possibile chiave
def test_key(key):
    decrypted_message = decrypt_message(encrypted_message, key)
    # Verifica se il risultato decrittato sembra essere testo in chiaro valido
    if all(char in string.printable for char in decrypted_message):
        return decrypted_message
    return None

# Prova tutte le possibili chiavi da 1 a 255 (0 è escluso perché non avrebbe effetto)
for key in range(1, 256):
    key_char = chr(key)
    decrypted = test_key(key_char)
    if decrypted:
        print(f"Key: '{key_char}' (ASCII value: {key})")
        print(f"Decrypted message:\n{decrypted}")
        print("\n")