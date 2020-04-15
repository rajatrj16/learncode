# Write a Python function that checks whether a passed in string is palindrome or not.

def palindrome(mystring):
    if mystring == mystring[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome('madam')