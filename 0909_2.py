import random

vowel=['a','e','y','u','i','o']
cons=['q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
ln=['Chen','Brantford','Doll','Fire']

def generation_name(vowel,cons,num):
    i = 1
    while i < num :
        name = ''
        name += random.choice(ln) + ' '
        for x in range(0, 3):
            name += random.choice(cons)
            name += random.choice(vowel)

        yield name
        i += 1
for name in generation_name(vowel,cons,5):
    print(name)
