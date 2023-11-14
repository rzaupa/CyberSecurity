import string
import operator


with open("challenge.txt", "r") as file:
    text = ''.join(file.readlines())
"""
def remove_punctuation(input_string):
    translator = str.maketrans("", "", string.punctuation)
    result = input_string.translate(translator)
    return result

def freq(text):
    f={}
    for i in text:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    return f

text_wo_punctation=remove_punctuation(text).replace(' ','').replace('\n','')
f=freq(text_wo_punctation)

perc=[f[i]*100/len(text) for i in f]
perc.sort()
perc.reverse()

diz={}
for i in text:
    diz[i]=f[i]*100/len(text)

sorted_diz=dict(sorted(diz.items(),key=operator.itemgetter(1)))
print(sorted_diz)

#print(i,':',f[i]*100/len(text),'%')
"""
text=text.replace('L','E').replace('S','A').replace('P','R').replace('H','I').replace('E','O').replace('O','T').replace('A','N').replace('D','S').replace('X','L').replace('Y','C').replace('U','U').replace('R','D').replace('W','P').replace('M','M').replace('V','H').replace('C','G').replace('N','B').replace('K','F').replace('Z','Y').replace('Q','W').replace('F','K').replace('T','V').replace('G','X').replace('B','Z').replace('J','J').replace('Q','Q')

print(text)