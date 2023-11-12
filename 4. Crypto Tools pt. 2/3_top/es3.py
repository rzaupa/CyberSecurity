#processo è:
#-creare semem tramite cur_time per random
#-ottenere un messaggio
#-creare key lunga quando il messaggio di numeri ognuno che va da 0 a 255
#-creare c facendo lo xor tra ogni elemento di (messaggio + tempo corrente, chiave + [0x88]*lunghezza di cur time)
#-scrivere i bytes di c

import random
import sys
import time

with open("top_secret","rb") as f:
    enc_bytes = f.read()
cur_time = str(time.time()).encode('ASCII')
random.seed(cur_time)

#gli ultimi len(cur_time) bytes sono il risultato dello xor tra cur_time e [0x88]*len(cur_time), si può ricavare cur_time facendo l'inverso
print(len(enc_bytes))

a=enc_bytes[-len(cur_time):]
l=[0x88]*len(cur_time)

cur_time_top_secret = ''.join([chr(m ^ k) for (m,k ) in zip(a,l)])

#ottenure cur_time possiamo ottenere la chiave
random.seed(cur_time_top_secret)
len_msg=len(enc_bytes)-len(cur_time_top_secret)
key=[random.randrange(256) for _ in range(len_msg)]

#con la chiave ora possiamo ottenere il messaggio
msg=''.join([chr(m^k) for (m,k) in zip(enc_bytes[:len_msg],key)])

print(msg)