import random

n = 0

laskuri = 0

N = int(input("Montako pistettä arvotaan?: "))

while laskuri < N:
    laskuri = laskuri + 1
    pisteetx = random.uniform(-1, 1)
    pisteety = random.uniform(-1, 1)

    if pisteetx**2 + pisteety**2 < 1:
        n = n + 1

laskenta = 4 * n / N
print(laskenta)




