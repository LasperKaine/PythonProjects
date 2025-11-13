from flask import Flask, jsonify
import mariadb

app = Flask(__name__)

def get_connection():
    try:
        conn = mariadb.connect(
            user="kasper",
            password="ahb8fee7",
            host="localhost",
            port=3306,
            database="flight_game",
            autocommit=True
        )
        return conn
    except mariadb.Error as e:
        print(f"Virhe tietokantayhteydessä: {e}")
        return None

@app.route('/kenttä/<string:icao>', methods=['GET'])
def hae_kentta(icao):
    conn = get_connection()
    if not conn:
        return jsonify({"error": "Tietokantayhteyttä ei voitu muodostaa."}), 500

    cur = conn.cursor()
    cur.execute("SELECT ident, name, municipality FROM airport WHERE ident = ?", (icao.upper(),))
    tulos = cur.fetchone()
    conn.close()

    if tulos:
        vastaus = {
            "ICAO": tulos[0],
            "Name": tulos[1],
            "Municipality": tulos[2]
        }
        return jsonify(vastaus)
    else:
        return jsonify({"error": f"Lentokenttää ICAO-koodilla '{icao}' ei löytynyt."}), 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
