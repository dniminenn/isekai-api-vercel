from http.server import BaseHTTPRequestHandler
import requests
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        url = "https://polygon-rpc.com"
        data = {
            "jsonrpc": "2.0",
            "method": "eth_call",
            "id": 1,
            "params": [
                {
                    "to": "0x449460B019eC80787660E665AAe42b920A33764F",
                    "data": "0x18160ddd"
                },
                "latest"
            ]
        }

        response = requests.post(url, json=data)
        result = json.loads(response.text)

        total_supply_hex = result.get("result", "")
        total_supply = int(total_supply_hex, 16)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str(total_supply).encode())
        return
