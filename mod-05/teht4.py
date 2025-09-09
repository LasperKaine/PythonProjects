lista = []

for i in range(5):
    kaupunginNimet = input("Kaupungin nimet: ")
    lista.append(kaupunginNimet)

for item in lista:
    print('\n'.join(lista))

