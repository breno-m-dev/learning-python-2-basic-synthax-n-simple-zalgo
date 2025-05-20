#this code is meant to be just some synthax tests to learn the basics
#I will try to make a simple Zalgo(glitchy text), by concateneting some diacritics into a string

the_str = 'a'
zalgo = True
if(zalgo==True):
    print('zalgo text will appear soon!')

diacritics = ["^", "~", "'"]

for diacritic in diacritics:
    the_str = the_str+diacritic

print(the_str)