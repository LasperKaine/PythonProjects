luvut = []

while True:

    luku = input("Anna luku: ")

    if luku == "":

        break

    luvut.append(luku)

print("Pienin: ", min(luvut), "Isoin: ", max(luvut))



