import random

numero = random.randint(1, 10)

while True:
    kysely = int(input("Arvaa luku 1-10: "))

    if kysely == numero:
        print("Oikein.")
        break

    if kysely > numero:
        print("Liian suuri arvaus. ")

    if kysely < numero:
        print("Liian pieni arvaus. ")
