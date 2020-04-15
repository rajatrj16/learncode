# Printing a pattern
#
#   *
# *   *
# *****
# *   *
# *   *

def patter(letter):
    patterns = {1: '   *   ', 2: '*     *', 3: '*******', 4: '*****', 5: '*  *', 6: '*    *'}
    alphabet = {'A': [1, 2, 3, 2, 2], 'R': [4, 2, 4, 5, 6]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])


patter('R')
