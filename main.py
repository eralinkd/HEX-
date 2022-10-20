from indians import *

while True:
    print("[1] - Перетворення значення HEX в Little Endian значення")
    print("[2] - Перетворення значення HEX на Big Endian значення")
    print("[3] - Перетворення значення Little Endian на HEX значення")
    print("[4] - Перетворення BIG Endian значення в HEX значення")
    k = input()
    if k == "1":
        test = int(input("Введіть значення HEX: "), 16)
        a = hex(test)
        print("Little Endian значення -", hex_to_little_endian(a))
    if k == "2":
        test = int(input("Введіть значення HEX: "), 16)
        a = hex(test)
        print("Big Endian значення -", hex_to_big_endian(a))
    if k == "3":
        test = int(input("Введіть значення Little Endian: "))
        size = int(input("Введіть кількість байтів: "))
        print("HEX значення -", little_endian_to_hex(test, size))
    if k == "4":
        test = int(input("Введіть значення Big Endian: "))
        print("HEX значення -", big_endian_to_hex(test))
    print()
