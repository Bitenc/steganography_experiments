def make_even( number ):
    if (number >= 255):
        return 254
    elif (number % 2 > 0):
        return number + 1
    else:
        return number

def make_odd( number ):
    if (number >= 255):
        return 255
    elif (number % 2 == 0):
        return number + 1
    else:
        return number