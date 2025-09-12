lentokentat = {
    "EFHK": "Helsinki-Vantaa",
    "EFET": "Enontekiö",
    "EFIV": "Ivalo",
    "EFJO": "Joensuu",
    "EFJY": "Jyväskylä",
    "EFKI": "Kajaani",
    "EFKT": "Kittilä",
    "EFKU": "Kuopio",
    "EFLP": "Lappeenranta",
    "EFMA": "Maarianhamina",
    "EFKE": "Kemi-Tornio",
    "EFKS": "Kuusamo",
    "EFPO": "Pori",
    "EFRO": "Rovaniemi",
    "EFSA": "Savonlinna",
    "EFTP": "Tampere-Pirkkala",
    "EFTU": "Turku",
    "EFVA": "Vaasa",
    "EFKU": "Kuopio",
    "EFOU": "Oulu"
}

while True:
    valinta = input("Valitse (uusiLentoasema) (haeLentoasema) (lopeta) ")

    if valinta == "uusiLentoasema":
        koodi = input("Anna ICAO-Koodi: ")
        nimi = input("Anna lentokentän nimi: ")
        lentokentat[koodi] = nimi

    if valinta == "haeLentoasema":
        koodi2 = input("Anna ICAO-Koodi: ")
        print(lentokentat[koodi2])

    if valinta == "lopeta":
        print("Lopetetaan ohjelma.")
        break
