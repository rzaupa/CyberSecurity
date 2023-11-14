import binascii
import base64
import string

ALPHABET = list(string.printable)   # len = 100
LEN = len(ALPHABET)

with open("encrypted_flag.txt", "r") as f:
   text = f.read()
   f.close()

FLAG = ""

# a useless method that could be replaced by a single line of code
# why not?
def hex_to_ascii(encoded):
    decoded = binascii.unhexlify(encoded)
    return decoded

def XORdecode(message, KEY="c4mPar1"):
    rep = len(message)//len(KEY) + 1
    key = (KEY*rep)[:len(message)] # adjust the key len
    xored = ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(message, key)])
    return xored
   
def ROTencode(message, pos):
    rot13_enc = ''
    for c in message:
        i = ALPHABET.index(c)
        rot13_enc += ALPHABET[(i-pos)%LEN]
    return rot13_enc

def base32decode(message):
    message_bytes = message.encode('ascii')
    b32_bytes = base64.b32decode(message_bytes) # here changes to decode
    b32_message = b32_bytes.decode('ascii')
    return b32_message

def base64decode(message):
    message_bytes = message.encode('ascii')
    b64_bytes = base64.b64decode(message_bytes)
    b64_message = b64_bytes.decode('ascii')
    return b64_message

hex_encrypted = hex_to_ascii(text)
decoded = XORdecode(hex_encrypted.decode('ascii'))

for _ in range(15):
    decoded = ROTencode(decoded, -3)
    decoded = base32decode(decoded)
    decoded = ROTencode(decoded, -13)
    decoded = base64decode(decoded)


print(decoded)