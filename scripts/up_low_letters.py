# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

def up_low(mystring):
    up = 0
    upl = ''
    low = 0
    lowl = ''
    ex = 0
    exl = ''
    for s in mystring:
        if s.isupper():
            up = up+1
            upl+=s
        elif s.islower():
            low = low+1
            lowl+=s
        else:
            ex+=1
            exl+=s
            ext = "'".join(exl)

    print(f'no of upper case "{upl}" : {up}')
    print(f'no of lower case "{lowl}": {low}')
    print(f'no of extras "{ext}": {ex}')

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')