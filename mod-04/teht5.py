kayttajaTunnus = "python"
salasana = "rules"
yritykset = 0

while True:
    kayttajaTunnusKysely = input("Anna käyttäjätunnus: ")
    salasanaKysely = input("Anna salasana: ")

    if kayttajaTunnus != kayttajaTunnusKysely or salasana != salasanaKysely:
        print("Käyttäjätunnus tai salasana väärin")
        yritykset = yritykset + 1

    if kayttajaTunnus == kayttajaTunnusKysely and salasana == salasanaKysely:
        print("Tervetuloa")
        break

    if yritykset == 5:
        print("Pääsy evätty")
        break





