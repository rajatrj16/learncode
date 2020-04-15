# Write a function that checks whether a number is in a given range (inclusive of high and low)

def inrange(num, low, high):
    if num >= low and num <= high:
        # return True
        print(f'{num} in in the range between {low} and {high}')
    else:
        print("not")


def inrange_bool(num, low, high):
    return num in range(low, high+1)


inrange(5, 11, 7)
inrange_bool(5, 2, 7)
