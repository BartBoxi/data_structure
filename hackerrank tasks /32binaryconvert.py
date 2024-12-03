n = 45

empty = []

def to_32(n):
    a = format(n, '032b')

    print("original",a)
    flipped = ''
    for bit in a:
        if bit == '0':
            flipped += '1'
        else:
            flipped += '0'
    decimal = int(flipped, 2)
    print(decimal)


to_32(n)

