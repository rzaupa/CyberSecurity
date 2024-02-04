text=open('description.txt','r').read()
message=text.split('\n')[0].split(' ')[-1]

def caesar_decrypt(text,from_,to_):
    for i in range(from_,to_):
        new_text=''.join([chr(ord(c)+i) for c in text])
        print(f"Key {i}\t{new_text}")

print(caesar_decrypt(message,-30,30))

#utilizzare vigenere solver