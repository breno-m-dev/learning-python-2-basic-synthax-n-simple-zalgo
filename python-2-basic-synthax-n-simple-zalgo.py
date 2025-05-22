#this code is meant to be just some synthax tests to learn the basics
#I will try to make a simple Zalgo(glitchy text), by concateneting some diacritics into a string
import random

zalgo = True
if(zalgo==True):
    print('zalgo text will appear soon!')



#\u0300 = grave `
#\u302 = circumflex ^
#\u303 = tilde ~
## usar isso da no mesmo que a linha de baixo!! diacritics = ["\u0300","\u0302", "\u0303","\u0300","\u0302", "\u0303","\u0300","\u0302", "\u0303","\u0300","\u0302", "\u0303" ]
#diacritics = ["\u0300","\u0302", "\u0303"]

#diacríticos que ficam acima dos carctéres
zalgo_up = [
    '\u030d', '\u030e', '\u0304', '\u0305', '\u033f', '\u0311', '\u0306',
    '\u0310', '\u0352', '\u0357', '\u0351', '\u0307', '\u0308', '\u030a',
    '\u0342', '\u0343', '\u0344', '\u034a', '\u034b', '\u034c', '\u0303',
    '\u0302', '\u030c', '\u0350', '\u0300', '\u0301', '\u030b', '\u030f',
    '\u0312', '\u0313', '\u0314', '\u033d', '\u0309', '\u0363', '\u0364',
    '\u0365', '\u0366', '\u0367', '\u0368', '\u0369', '\u036a', '\u036b',
    '\u036c', '\u036d', '\u036e', '\u036f'
]
#diacríticos que ficam abaixo dos caractéres
zalgo_down = [
    '\u0316', '\u0317', '\u0318', '\u0319', '\u031c', '\u031d', '\u031e',
    '\u031f', '\u0320', '\u0324', '\u0325', '\u0326', '\u0329', '\u032a',
    '\u032b', '\u032c', '\u032d', '\u032e', '\u032f', '\u0330', '\u0331',
    '\u0332', '\u0333', '\u0339', '\u033a', '\u033b', '\u033c', '\u0345',
    '\u0347', '\u0348', '\u0349', '\u034d', '\u034e', '\u0353', '\u0354',
    '\u0355', '\u0356', '\u0359', '\u035a'
]


input ="oioi tudo bem?"
outputStr =""

for char in input:
    outputStr += char #adiciona 1 char a string de saida
    for i in range(5): #adiciona os diacriticos no ultima char adicionado a string de saida
        outputStr +=  zalgo_up[random.randrange(0,len(zalgo_up))] #seleciona um diacritico aleatório
        outputStr +=  zalgo_down[random.randrange(0,len(zalgo_down))] #seleciona um diacritico aleatório

print("Output:"+outputStr)