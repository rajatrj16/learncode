# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_lists(ulist):
    a = []
    for l in ulist:
        if l not in a:
            a.append(l)
    print(a)


unique_lists([1,1,1,1,2,2,3,3,3,3,4,5])