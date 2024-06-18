# CyberSecurity

Esercizi del corso Cybersecurity: principles and practices A.A. 2023/24

Es non risolti:

- CT pt. 1 es 4
- CT pt. 2 es 4 parte 2
- IoW es 2-3
- LV es 1-2-3
- WI es 1-2-3-4

## Utili

https://github.com/obviouslynotraffa/Cybersecurity.git

### Reverse

Usare IDA

Rendere eseguibile un file

- tasto destro e mettere la spunta su eseguibile
- lanciare il comando chmod u+x nomefile
- eseguire il file con ./nomefile

Visualizzare le informazioni dai file oggetto:

- objdump -d nomefile

Assembly:

- cmp : confronta due campi statici numerici

Conversione:

- da esa to decimale , da decimale to ascii

Patching:

1. Fate clic su 'jnz': ora dovrebbe essere evidenziato; 
2. Andate su: Edit > Patch program > Assemble (e si modifica singolarmente la linea di assembly che contiene jnz, cliccandola e premendo OK)
3. Scrivete "jz short loc_994";
4. Premere OK.

In questo modo abbiamo modificato manualmente il flusso di esecuzione del nostro programma. Dobbiamo solo applicare questa patch al programma originale... e voilà!Per applicare la patch al programma, procedere come segue:

1. Edit > Patch program > Apply patches to input file...
2. Confermare l'operazioneCiò è evidente comunque evidenziando cosa fa il codice:


Debugging:

1. gdb nomefile
2. break main
3. run o r
4. jump nomefunzione
5. disas main

### PLTGOT

avere gdb-peda e fare checksec per valutare RELRO
usare radare2

### Assemblyò

Movimento dei dati:

- MOV: Trasferisce dati da una posizione all'altra.
- LEA: Carica l'indirizzo effettivo di un operando nella destinazione.
- LDM, STM: Carica o memorizza dati in memoria.

Aritmetica:

- ADD, SUB: Somma o sottrae valori.
- MUL, DIV: Moltiplica o divide valori.
- INC, DEC: Incrementa o decrementa il valore di una variabile.

Controllo del flusso:

- JMP: Salto incondizionato a un'etichetta specifica.
- JE, JNE, JZ, JNZ: Istruzioni di salto condizionato.
- CMP: Compara due operandi.

Gestione delle stringhe:

- MOVSB, MOVSW, MOVSD: Spostano una stringa di byte, parole o doppie parole.
- LODSB, LODSW, LODSD: Caricano un byte, una parola o una doppia parola da una stringa.
- STOSB, STOSW, STOSD: Memorizzano un byte, una parola o una doppia parola in una stringa.

Chiamate di funzioni e Stack:

- CALL: Chiama una procedura o una funzione.
- RET: Restituisce il controllo dalla chiamata di una funzione.
- PUSH, POP: Inserisce o rimuove dati dallo stack.

I/O:

- IN, OUT: Legge o scrive da o verso una porta di I/O.
Altre istruzioni:

- NOP: Nessuna operazione.
- HLT: Arresta l'esecuzione del programma.

