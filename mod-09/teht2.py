class Auto:
    def __init__(self, rekisteri_tunnus, huippu_nopeus):
        self.rekisteri_tunnus = rekisteri_tunnus
        self.huippu_nopeus = huippu_nopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.tamanhetkinen_nopeus += muutos
        if self.tamanhetkinen_nopeus > self.huippu_nopeus:
            self.tamanhetkinen_nopeus = self.huippu_nopeus
        elif self.tamanhetkinen_nopeus < 0:
            self.tamanhetkinen_nopeus = 0

uusi_auto = Auto("ABC-123", 142)

uusi_auto.kiihdyta(30)
uusi_auto.kiihdyta(70)
uusi_auto.kiihdyta(50)

print(f"Auton nopeus: {uusi_auto.tamanhetkinen_nopeus} km/h")

uusi_auto.kiihdyta(-200)
print(f"Auton nopeus hätäjarrutuksen jälkeen: {uusi_auto.tamanhetkinen_nopeus} km/h")

