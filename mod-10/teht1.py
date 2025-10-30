class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen_kerros = alin

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

    def siirry_kerrokseen(self, kohde):
        if kohde > self.ylin or kohde < self.alin:
            print("Virhe: kerros ei ole sallittujen rajojen sisällä.")
            return

        print(f"Siirrytään kerrokseen {kohde}...")
        while self.nykyinen_kerros < kohde:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde:
            self.kerros_alas()


# --- Pääohjelma ---
if __name__ == "__main__":
    h = Hissi(1, 10)       # hissi, jossa alin kerros 1 ja ylin 10
    h.siirry_kerrokseen(5) # siirrytään kerrokseen 5
    h.siirry_kerrokseen(1) # palataan takaisin alimpaan kerrokseen
