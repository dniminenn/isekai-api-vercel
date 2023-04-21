from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import requests
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
        currency = query_params.get('currency', ['usd'])[0].lower()

        url = "https://api.dexscreener.com/latest/dex/pairs/polygon/0x47130c5227e478c393288295fc4d975580bd9cdf"
        response = requests.get(url)
        data = json.loads(response.text)

        if currency == 'matic':
            price = data.get("pair", {}).get("priceNative", "")
        else:  # Default to USD
            price = data.get("pair", {}).get("priceUsd", "")

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Cache-Control', 's-maxage=300, stale-while-revalidate')
        self.end_headers()
        self.wfile.write(str(price).encode())
        return
