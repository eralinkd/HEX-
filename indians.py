from sys import getsizeof


def hex_to_little_endian(a):
    a = a[2:][::-1]
    a = int("0x"+a, 16)
    a = str(hex(a))
    if len(a) % 2 == 1:
        a += "0"
    return int(a, 16)


def hex_to_big_endian(a):
    return int(a, 16)


def little_endian_to_hex(a, size):
    length = size*2
    a = hex(a)
    a += "0" * (length - len(a)+2)
    return a


def big_endian_to_hex(a):
    return hex(a)
