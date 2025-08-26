sukupuoli = input("Anna biologinen sukupuolesi: ")
hemoglobiini = int(input("Anna hemoglobiiniarvo (g/l): "))

if sukupuoli == "nainen" and hemoglobiini < 117:
    print("Hemoglobiiniarvosi on alhainen")

if sukupuoli == "nainen" and hemoglobiini > 175:
    print("Hemoglobiiniarvosi on korkea")

if sukupuoli == "nainen" and 117 <= hemoglobiini <= 175:
    print("Hemoglobiiniarvosi on normaali")

if sukupuoli == "mies" and hemoglobiini < 134:
    print("Hemoglobiiniarvosi on alhainen")

if sukupuoli == "mies" and hemoglobiini > 195:
    print("Hemoglobiiniarvosi on korkea")

if sukupuoli == "mies" and  134 <= hemoglobiini <= 195:
    print("Hemoglobiiniarvosi on normaali")

else:
    print("Väärät tiedot!")