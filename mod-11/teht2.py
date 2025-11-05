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

class Sahkoauto(Auto):
    def __init__(self, rekisteri_tunnus, huippu_nopeus, akkukapasiteetti):
        super().__init__(rekisteri_tunnus, huippu_nopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri_tunnus, huippu_nopeus, bensatankin_koko):
        super().__init__(rekisteri_tunnus, huippu_nopeus)
        self.bensatankin_koko = bensatankin_koko

if __name__ == "__main__":
    sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
    polttis = Polttomoottoriauto("ACD-123", 165, 32.3)

    sahkoauto.kiihdyta(120)
    polttis.kiihdyta(100)

    sahkoauto.kulje(3)
    polttis.kulje(3)

    print(f"{sahkoauto.rekisteri_tunnus}: {sahkoauto.kuljettu_matka:.1f} km (Akkukapasiteetti: {sahkoauto.akkukapasiteetti} kWh)")
    print(f"{polttis.rekisteri_tunnus}: {polttis.kuljettu_matka:.1f} km (Tankki: {polttis.bensatankin_koko} l)")
