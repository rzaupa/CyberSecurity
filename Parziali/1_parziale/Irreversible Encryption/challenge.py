#!/usr/bin/env python3

import base64
import string
import binascii

ALPHABET = list(string.printable)   # len = 100 
LEN = len(ALPHABET)

FLAG = "??????????????????????????????????????????????"

# b64 encoding is safe and my flag secure
def base64encode(message):
    message_bytes = message.encode('ascii')
    b64_bytes = base64.b64encode(message_bytes)
    b64_message = b64_bytes.decode('ascii')
    return b64_message

# same for b32
def base32encode(message):
    message_bytes = message.encode('ascii')
    b32_bytes = base64.b32encode(message_bytes)
    b32_message = b32_bytes.decode('ascii')
    return b32_message

# I think I'm forgetting something important to remove here
def XORencode(message, KEY="c4mPar1"):
    rep = len(message)//len(KEY) + 1
    key = (KEY*rep)[:len(message)] # adjust the key len
    xored = ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(message, key)])
    return xored

# Easy-to-use function, that looks useful
def ROTencode(ciphertext, pos):
    rot_dec = ''
    for c in ciphertext:
        if c in ALPHABET:
            i = ALPHABET.index(c)
            rot_dec += ALPHABET[(i - pos) % LEN]
        else:
            rot_dec += c  # Mantiene i caratteri non presenti nell'alfabeto invariati
    return rot_dec


# a useless method that could be replaced by a single line of code
# why not?
def ascii_to_hex(message):
    encoded = binascii.hexlify(message).decode()
    return encoded

# do it 15 times plz
encrypted = "Encode as if there's no tomorrow: " + FLAG
for _ in range(15):
    # encode the FLAG in the 4 different ways, always the same order
    b64_encrypted = base64encode(encrypted)
    rot13_encrypted = ROTencode(b64_encrypted, 13)
    b32_encrypted = base32encode(rot13_encrypted)
    encrypted = ROTencode(b32_encrypted, 3)

#  I was told that XOR is a secure operation
xor_encrypted = XORencode(encrypted).encode('ascii')

# hopefully also the hex encoding will strengthen the encryption operation
hex_encrypted = ascii_to_hex(xor_encrypted)

# save the result for later use
# none will decrypt it anyway
with open("encrypted_flag.txt", "w") as f:
    f.write(hex_encrypted)
    f.close()

# ascii_encrypted
ascii_encrypted = binascii.hexlify(encrypted.encode()).decode()
