#this code is meant to be just some synthax tests to learn the basics
#I will try to make a simple Zalgo(glitchy text), by concateneting some diacritics into a string

the_str = 'a'
zalgo = True
if(zalgo==True):
    print('zalgo text will appear soon!')

#\u0300 = grave `
#\u302 = circumflex ^
#\u303 = tilde ~
## usar isso da no mesmo que a linha de baixo!! diacritics = ["\u0300","\u0302", "\u0303","\u0300","\u0302", "\u0303","\u0300","\u0302", "\u0303","\u0300","\u0302", "\u0303" ]
diacritics = ["\u0300","\u0302", "\u0303"]
input ="oioi tudo bem?"
outputStr =""

for char in input:
    outputStr += char #adiciona 1 char a string de saida
    for diacritic in diacritics: #adiciona os diacriticos no ultima char adicionado a string de saida
        outputStr += diacritic 

print(the_str)
print("Output:"+outputStr)