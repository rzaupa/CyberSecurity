# CyberSecurity

Esercizi del corso Cybersecurity: principles and practices A.A. 2023/24

Es non risolti:

- CT pt. 1 es 4
- CT pt. 2 es 4 parte 2
- IoW es 2-3
- LV es 1-2-3
- WI es 1-2-3-4

## Utili

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
