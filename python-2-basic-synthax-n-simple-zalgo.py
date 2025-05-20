#this code is meant to be just some synthax tests to learn the basics
#I will try to make a simple Zalgo(glitchy text), by concateneting some diacritics into a string

the_str = 'a'
zalgo = True
if(zalgo==True):
    print('zalgo text will appear soon!')


#\u0300 = grave `
#\u302 = circumflex ^
#\u303 = tilde ~
diacritics = ["\u0300","\u0302", "\u0303" ]

for diacritic in diacritics:
    the_str = the_str+diacritic

print(the_str)