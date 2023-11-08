textss = open("book.txt", "r").read()

paragrapsss=textss.split('\n\n')

liness=[]
for i in range(len(paragrapsss)):
   liness.append(paragrapsss[i].split('\n'))

list=[
    [0, 8, 3],
    [3, 1, 7],
    [3, 7, 2],
    [6, 0, 4],
    [7, 9, 0]
]
frase=''
for el in list:
      frase=frase + ' ' + (liness[el[0]][el[1]].split(' ')[el[2]])
      
print(frase)

# (1, 9, 4) (4, 2, 8) (4, 8, 3) (7, 1, 5) (8, 10, 1)

