class Auto:
    def __init__(self, rekisteri_tunnus, huippu_nopeus):
        self.rekisteri_tunnus = rekisteri_tunnus
        self.huippu_nopeus = huippu_nopeus
        self.tamanhetkinen_nopeus = 60
        self.kuljettu_matka = 2000

    def kiihdyta(self, muutos):
        self.tamanhetkinen_nopeus += muutos
        if self.tamanhetkinen_nopeus > self.huippu_nopeus:
            self.tamanhetkinen_nopeus = self.huippu_nopeus
        elif self.tamanhetkinen_nopeus < 0:
            self.tamanhetkinen_nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.tamanhetkinen_nopeus * tunnit

uusi_auto = Auto("ABC-123", 60)

uusi_auto.kiihdyta(30)
uusi_auto.kiihdyta(70)
uusi_auto.kiihdyta(50)

print(f"Auton nopeus: {uusi_auto.tamanhetkinen_nopeus} km/h")

uusi_auto.kulje(1.5)

print(f"Kuljettu matka: {uusi_auto.kuljettu_matka} km")

uusi_auto.kiihdyta(-200)
print(f"Auton nopeus hätäjarrutuksen jälkeen: {uusi_auto.tamanhetkinen_nopeus} km/h")

