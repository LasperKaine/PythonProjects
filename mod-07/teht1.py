vuodenAjat = ("kevät", "kesä", "syksy", "talvi")

kuukaudenNumero = int(input('Anna kuukauden numero: '))

lasku = ((kuukaudenNumero - 3) % 12) // 3

vuodenAika = vuodenAjat[lasku]

print(f"{kuukaudenNumero}. Vuoden aika on {vuodenAika}.")

