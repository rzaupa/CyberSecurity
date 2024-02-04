from multiprocessing import process
from pwn import *

p = process('./vuln')
msg = 'here put your message'
p.sendline(msg)
p.interactive()