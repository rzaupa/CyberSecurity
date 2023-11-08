text=open("description.txt","r").read()
first_line=text.split('\n')[0].split(',')[1]
last_line=text.split('\n')[-2].split(' ')[1]

#base64 to ASCII
import base64
def base64tostring(textb64):
    return base64.b64decode(textb64).decode('utf-8',errors="ignore")

last_string=base64tostring(last_line)
first_string=base64tostring(first_line)
print(last_string)
print(first_string)

def caesar_decrypt(text,from_,to_):
    for i in range(from_,to_):
        new_text=''.join([chr(ord(c)+i) for c in text])
        print(f"Key {i}\t{new_text}")

# Esempio di utilizzo
caesar_decrypt(last_string,-30,30)
#il flag -24 mi sembra sensato
solution=''.join([chr(ord(c)-24) for c in last_string])

print("Soluzione",solution)

