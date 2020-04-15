# Create a otp no.


def otp(number):

    legth = len(number)

    otp = ""

    for odd in range(1, legth, 2):

        otp += str(int(number[odd])**2)

    print otp[0:4]

number = "123456"

otp(number)
