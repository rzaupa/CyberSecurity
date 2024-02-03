with open("encrypted.txt", 'r') as f:
    text_hex = f.read()

#------------------------------------STEP 1-------------------------------------------------
#TESTO ESADECIMALE -> DECIMALE 
def hex2dec(text):
    res = []
    for i in range(0, len(text), 2):
        #get the current pair of hex
        curr = text[i:i+2]

        #convert to int
        if curr != '\n':
            res.append(int(curr, 16))

    return res

text_dec=hex2dec(text_hex)

#DEFINIZIONE FUNZIONE SHIFT
def shift(text,key_len):
    new_text=text[key_len:]+text[:key_len]
    return new_text

#DEFINIZIONE FUNZIONE FREQUENZA per calcolare i numeri che sono rimasti nella stessa posizione
def freq(text,new_text):
    freq=0
    for i in range(len(text)):
        if text[i]==new_text[i]:
            freq=freq+1
    return freq

#DEFINIZIONE FUNZIONE TROVA LUNGHEZZA CHIAVE in base alla frequenza massima
def find_key_len(text,_from=6,_to=16):
    f_max=0
    kl_opt=0
    for kl in range(_from,_to):
        new_text=shift(text,kl)
        f=freq(text,new_text)
        if f>f_max:
            f_max=f
            kl_opt=kl
    return kl_opt


#-------------------------------------------STEP 2------------------------------------------------------
