kuhanPituus = float(input("Kuhan pituus (senttimetreinä): "))
sallittuPituus = 37

if kuhanPituus < sallittuPituus:
    print("Laske kuha takaisin järveen!")
    print("Sallitusta painosta puuttuu: ", (sallittuPituus - kuhanPituus))