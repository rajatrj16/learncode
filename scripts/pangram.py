# Write a Python function to check whether a string is pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

import string

def panagram(mystring):
    if len(set(mystring.lower().replace(' ', ''))) == len(string.ascii_lowercase):
        print('Panagram')
    else:
       print('Not Panagram')

panagram('The quick brown fox jumps over the kazy dog')