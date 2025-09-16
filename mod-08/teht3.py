import mariadb
from geopy.distance import geodesic

def hae_koordinaatit(conn, icao):
    cur = conn.cursor()
    cur.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident=?", (icao,))
    tulos = cur.fetchone()
    if tulos:
        return (tulos[0], tulos[1])  # (lat, lon)
    else:
        return None

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

icao1 = input("Anna ensimmäinen ICAO-koodi: ").upper()
icao2 = input("Anna toinen ICAO-koodi: ").upper()

koord1 = hae_koordinaatit(conn, icao1)
koord2 = hae_koordinaatit(conn, icao2)

if not koord1 or not koord2:
    print("Jompikumpi ICAO-koodi ei löytynyt tietokannasta.")
else:
    etaisyys = geodesic(koord1, koord2).kilometers
    print(f"Etäisyys kenttien {icao1} ja {icao2} välillä on {etaisyys:.2f} km.")
