textss = open("challenge.txt", "r").read()
flag=''
for c in textss:
    if c.isupper():
        flag=flag+c

flag=flag.replace('ZERO','0')
flag=flag.replace('ONE','1')

flag=int(flag,base=2)
flag = flag.to_bytes((flag.bit_length() + 7)//8, 'big').decode()
#flag=int(flag,2)

print(flag)
