# Write a Python function to multiply all the numbers in a list.


def multiply_all(nums):
    total = 1
    for n in nums:
        total = total * n
    print(total)

multiply_all([1,2,3,-4])