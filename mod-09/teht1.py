class Auto:
    def __init__(self, rekisteri_tunnus, huippu_nopeus):
        self.rekisteri_tunnus = rekisteri_tunnus
        self.huippu_nopeus = huippu_nopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

uusi_auto = Auto("ABC-123", 142)

print(f"Rekisteritunnus: {uusi_auto.rekisteri_tunnus}")
print(f"Huippunopeus: {uusi_auto.huippu_nopeus} km/h")
print(f"Tämänhetkinen nopeus: {uusi_auto.tamanhetkinen_nopeus} km/h")
print(f"Kuljettu matka: {uusi_auto.kuljettu_matka} km")


