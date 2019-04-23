def hexad (n):

    d = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}

    a = str(int(n)%16)

    b = str(int((int(n)/16)%(16)))

    c = str(int(int(n)/(16*16)))


    if int(a) > 9:
        a = d[int(a)]

    if int(b) > 9:
        b = d[int(b)]

    if int(c) > 9:
        c = d[int(c)]

    s = c+b+a

    return s


