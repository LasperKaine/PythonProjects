import mariadb

def hae_ICAO_koodi(conn, icao):
    cur = conn.cursor()
    cur.execute("SELECT name, municipality FROM airport WHERE ident=?", (icao,))
    tulos = cur.fetchall()
    if cur.rowcount > 0:
        for rivi in tulos:
            print(f"{icao}: {rivi[0]} (sijaintikunta: {rivi[1]})")
    else:
        print("Ei löytynyt lentokenttää annetulla ICAO-koodilla.")

try:
    conn = mariadb.connect(
        user="kasper",
        password="ahb8fee7",
        host="localhost",
        port=3306,
        database="flight_game",
        autocommit=True
    )
    print("Yhteys onnistui!")
except mariadb.Error as e:
    print(f"Virhe yhteydessä MariaDB:hen: {e}")
    exit(1)

icao = input("Anna ICAO-koodi: ")
hae_ICAO_koodi(conn, icao)
