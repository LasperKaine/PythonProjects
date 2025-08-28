tuuma = int(input("Anna tuuma: "))

while tuuma > 0:

    tuumaMuunnin = 2.54

    print(tuuma * tuumaMuunnin)

    tuuma = int(input("Anna tuuma: "))

    if tuuma < 0:
        break

print("Ohjelma lopetettu!")
