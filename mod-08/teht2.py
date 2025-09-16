import mariadb

def hae_maa_koodi(conn, iso_country):
    cur = conn.cursor()
    cur.execute("""
        SELECT type, COUNT(*) 
        FROM airport 
        WHERE iso_country = ? 
        GROUP BY type
    """, (iso_country,))
    tulos = cur.fetchall()
    if cur.rowcount > 0:
        print(f"Lentokentät maassa {iso_country}:")
        for tyyppi, lkm in tulos:
            print(f"{tyyppi}: {lkm} kpl")
    else:
        print("Ei löytynyt lentokenttiä annetulla maakoodilla.")

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

maa = input("Anna maakoodi (esim. FI): ").upper()
hae_maa_koodi(conn, maa)
