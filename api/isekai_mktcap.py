from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import requests
import json


def fetch_dexscreener_data():
    url = "https://api.dexscreener.com/latest/dex/pairs/polygon/0x47130c5227e478c393288295fc4d975580bd9cdf"
    response = requests.get(url)
    return json.loads(response.text)


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = fetch_dexscreener_data()
        market_cap = data.get("pair", {}).get("fdv", "")

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Cache-Control', 's-maxage=300, stale-while-revalidate')
        self.end_headers()
        self.wfile.write(str(market_cap).encode())
        return