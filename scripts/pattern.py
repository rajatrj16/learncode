# # # #
# # # #
# # # #
# # # #
from time import sleep


def hash1(n):
    for i in range(0, n):
        for j in range(0, n):
            print('# ', end="")
        print()


hash1(4)
print()

def hash2(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print('# ', end="")
        print()


hash2(4)
print()

def hash3(n):
    for i in range(0, n):
        for j in range(0, n-i):
            print('# ', end="")
        print()


hash3(4)
print()

def hash4(n):
    for i in range(0, n):
        for j in range(0, n-i):
            print(" ", end="")
        for j in range(0, i+1):
            print("# ", end="")
        print()
hash4(4)
print()

def hash5(n):
    for i in range(n):
        for i in range(i+1):
            print(i, end="")
        print()
hash5(4)
print()

def hash6(n):
    for i in range(n):
        for j in range(n):
            print(i, end="")
        print()
hash6(4)
print()

def hash7(n):
    num = 1
    for i in range(n):
        for j in range(i+1):
            print(num, end=" ")
            num = num + 1
        print()
hash7(4)
print()

def hash8(n):
    num = 65
    for i in range(n):
        for j in range(i+1):
            ch = chr(num)
            print(ch, end=" ")
            num = num + 1
        print()
hash8(4)
print()

def hash9(n):
    num = 65
    for i in range(n):
        for j in range(i+1):
            ch = chr(num)
            print(ch, end=" ")
        num = num + 1
        print()
hash9(4)

# def revhash4(n):
#     if hash4(n)=="#":
#         print(" ")
#     else:
#         print("#")
# revhash4(4)