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


autot = []
for i in range(1, 11):
    huippu_nopeus = random.randint(100, 200)
    rekisteri_tunnus = f"ABC-{i}"
    autot.append(Auto(rekisteri_tunnus, huippu_nopeus))

# Kilpailu alkaa
kilpailu_kaynnissa = True
tunti = 0

while kilpailu_kaynnissa:
    tunti += 1
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)
        auto.kulje(1)
        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False
            break

print(f"\nKilpailu päättyi {tunti} tunnin jälkeen!\n")
print(f"{'Rekisteri':<10}{'Huippunopeus':<15}{'Nopeus':<15}{'Matka':<15}")
print("-" * 55)
for auto in autot:
    print(f"{auto.rekisteri_tunnus:<10}{auto.huippu_nopeus:<15}{auto.tamanhetkinen_nopeus:<15}{auto.kuljettu_matka:<15.1f}")
