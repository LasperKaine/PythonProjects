import random

tyhjaKolme = ""
tyhjaNelja = ""


for i in range(3):
    pinKolme = (random.randint(0, 9))
    tyhjaKolme += str(pinKolme)

print(tyhjaKolme)

for i in range(4):
    pinNelja = (random.randint(1, 6))
    tyhjaNelja += str(pinNelja)

print(tyhjaNelja)

