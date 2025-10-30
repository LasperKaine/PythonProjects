import random

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

    def kulje(self, tunnit):
        self.kuljettu_matka += self.tamanhetkinen_nopeus * tunnit


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n{'Rekisteri':<10}{'Huippunopeus':<15}{'Nopeus':<15}{'Matka':<15}")
        print("-" * 55)
        for auto in self.autot:
            print(f"{auto.rekisteri_tunnus:<10}{auto.huippu_nopeus:<15}{auto.tamanhetkinen_nopeus:<15}{auto.kuljettu_matka:<15.1f}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False


if __name__ == "__main__":
    autot = []
    for i in range(1, 11):
        huippu_nopeus = random.randint(100, 200)
        rekisteri_tunnus = f"ABC-{i}"
        autot.append(Auto(rekisteri_tunnus, huippu_nopeus))

    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    tunti = 0
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunti += 1
        if tunti % 10 == 0:
            print(f"\nTunti {tunti} – tilanne kilpailussa '{kilpailu.nimi}':")
            kilpailu.tulosta_tilanne()

    print(f"\nKilpailu '{kilpailu.nimi}' päättyi {tunti} tunnin jälkeen!")
    print("Lopputilanne:")
    kilpailu.tulosta_tilanne()
