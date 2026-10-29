# missioner and cannibals 

m = 3
c = 3

while m > 0 or c > 0:
    if c == 3:
        c = c - 2
        print("2 Cannibals cross")

    elif c == 1:
        c = c + 1
        print("1 Cannibal returns")

    elif c == 2 and m == 3:
        c = c - 2
        print("2 Cannibals cross")

    elif c == 0 and m == 3:
        m = m - 2
        print("2 Missionaries cross")

    else:
        break

    print("Missionaries left:", m)
    print("Cannibals left:", c)
