vuosi = int(input("Anna vuosi: "))
while vuosi >= 1896:

    if vuosi % 4 == 0:
        print("Olympia vuosi.")

    else:
        print("Ei olympia vuosi.")


    vuosi = int(input("Anna vuosi: "))

if vuosi < 1896:
    print("Ennen moderneja olympialaisia.")

print("Ohjelmisto suoritettu.")

