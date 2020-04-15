def reverse(str):
    return str[::-1]


def checkrev(str):
    rev = reverse(str)

    if str == rev:
        print ("Yes")
    else:
        print("No")


checkrev("VAVDD")

