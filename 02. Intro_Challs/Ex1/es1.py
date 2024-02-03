string=input("Inserisci una stringa ")
new_string=''
for i in range(0,len(string)):
   new_string=new_string+chr(ord(string[i])+2)

print(new_string)