def gallona_litra(gallona):
    return gallona * 3.785

while True:
    gallona = float(input("Anna bensiinin määrä gallonoina (negatiivinen lopettaa): "))
    if gallona < 0:
        print("Lopetetaan ohjelma.")
        break
    litraa = gallona_litra(gallona)
    print(f"{gallona} gallonaa on {litraa:.2f} litraa.")
