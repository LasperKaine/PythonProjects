import random

def heita_noppa(tahkot):
    return random.randint(1, tahkot)

max_silmaluku = int(input("Anna nopan maksimisilmäluku: "))

while True:
    silmaluku = heita_noppa(max_silmaluku)
    print(f"Heitto: {silmaluku}")
    if silmaluku == max_silmaluku:
        break
