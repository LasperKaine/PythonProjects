lista = []

for i in range(5):
    kaupunginNimet = input("Kaupunginni nimet: ")
    lista.append(kaupunginNimet)

for item in lista:
    print('\n'.join(lista))

