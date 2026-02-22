def taxi(dist):
    m = dist * 1000
    parts = m / 140
    summa = 4 + parts * 0.25
    return summa

var = 8
km = int(input())
print(taxi(km * var))