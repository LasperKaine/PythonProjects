kokonaisluku = int(input("Anna kokonaisluku: "))

if kokonaisluku < 2:
    print("Ei ole alkuluku")
else:
    on_alkuluku = True
    for i in range(2, kokonaisluku):
        if kokonaisluku % i == 0:
            on_alkuluku = False
            break
    if on_alkuluku:
        print("On alkuluku")
    else:
        print("Ei ole alkuluku")
