input1=int(input("Inserisci il primo numero intero "))
input2=int(input("Inserisci il secondo numero intero "))

print("Scegli dal seguente menu\n 1) 0 per addizione\n 2) 1 per sottrazione\n 3) 2 per moltiplicazione \n 4) 3 per divisione\n")

operation=int(input("Inserisci il numero associato all'operazione "))
if operation==0:
    print("Il risultato è ",input1+input2)
elif operation==1:
    print("Il risultato è ",input1-input2)
elif operation==2:
    print("Il risultato è ",input1*input2)
elif operation==3:
    if input2!=0:
        print("Il risultato è ",input1/input2)
    else:
        print("Errore, non si può dividere per 0")
else:
    print("Errore, numero dell'operazione non corretto")

