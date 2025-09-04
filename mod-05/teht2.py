summa = []

while True:
    luku = str(input("Anna luku: "))

    if luku == "":
        break

    summa.append(int(luku))

summa.sort(reverse=True)

print(summa[:5])
