leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

grammat = (leiviskat * 20 * 32 + naulat * 32 + luodit) * 13.3

kilogramma = int(grammat / 1000)
gramma = round(grammat % 1000, 2)

print("Massa mittojen mukaan: ", kilogramma , "kilogrammaa " "ja", gramma , "grammaa.")