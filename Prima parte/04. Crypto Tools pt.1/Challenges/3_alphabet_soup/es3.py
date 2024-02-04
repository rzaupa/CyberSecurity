message=open('encrpyted.txt','r').read()

freq={}
for m in message:
    if m not in freq:
        freq[m]=1
    else:
        freq[m]+=1

message=message.replace('K','i').replace('Q','m').replace('F','a').replace('W','f').replace('A','l').replace('I','g').replace('G','d').replace('P','y').replace('D','o').replace('T','u').replace('C','r').replace('M','n').replace('H','b').replace('N','t').replace('L','h').replace('B','s').replace('S','v').replace('U','e').replace('X','c').replace('V','w')

diff=ord('K')-ord('I')
diff1=ord('Q')-ord('M')

print(diff)
print(diff1)

print(message)
print(freq)