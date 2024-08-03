from flask import Flask, request, jsonify
import requests
import sqlite3

app = Flask(__name__)
GENIUS_API_URL = "https://api.genius.com"
GENIUS_ACCESS_TOKEN = "Gc-qzUIlM6QMTibFS-H1ccw-4_diU8e0lotyWqpQJ1do-WttVYVZIWIcTf_3G6Cd"


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    response = requests.get(f"{GENIUS_API_URL}/search",
                            headers={"Authorization": f"Bearer {GENIUS_ACCESS_TOKEN}"},
                            params={"q": query})
    return jsonify(response.json())


@app.route('/lyrics', methods=['GET'])
def get_lyrics():
    song_id = request.args.get('song_id')
    response = requests.get(f"{GENIUS_API_URL}/songs/{song_id}",
                            headers={"Authorization": f"Bearer {GENIUS_ACCESS_TOKEN}"})
    song_data = response.json()
    lyrics_path = song_data['response']['song']['path']
    lyrics_response = requests.get(f"https://genius.com{lyrics_path}")
    # Parse lyrics_response.text to extract lyrics (skipping for brevity)
    return jsonify(song_data)


if __name__ == '__main__':
    app.run(debug=True)
