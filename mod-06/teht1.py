import random

def heita_noppa():
    return random.randint(1, 6)

while True:
    silmaluku = heita_noppa()
    print(f"Heitto: {silmaluku}")
    if silmaluku == 6:
        break
