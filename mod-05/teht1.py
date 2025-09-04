import random

summa = 0
arpakuutiot = int(input("Anna arpakuutioiden lukumäärä: "))


for i in range(arpakuutiot):
    noppa = random.randint(1, 6)
    summa = summa + noppa

print(summa)




