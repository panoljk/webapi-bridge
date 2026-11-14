"""Local read-only sandbox — no exchange connectivity or live trading."""
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

HOST = "127.0.0.1"
PORT = int(os.environ.get("WEBAPI_BRIDGE_DEMO_PORT", "8787"))

class GatewayHandler(BaseHTTPRequestHandler):
    server_version = "WebAPIBridgeSandbox/0.1"

    def send_json(self, data, code=200):
        payload = json.dumps(data, separators=(",", ":")).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        parsed = urlparse(self.path)
        account = parse_qs(parsed.query).get("account", ["paper-main"])[0]
        if parsed.path == "/v1/health":
            return self.send_json({"ok": True, "mode": "sandbox", "live_trading": False})
        if parsed.path == "/v1/accounts":
            return self.send_json({"accounts": [{"id": "paper-main", "exchange": "simulated", "mode": "paper", "status": "connected"}]})
        if parsed.path in ("/v1/balances", "/v1/positions") and account != "paper-main":
            return self.send_json({"error": "unknown demo account"}, 404)
        if parsed.path == "/v1/balances":
            return self.send_json({"account": account, "currency": "USDT", "total": 10000.0, "free": 10000.0, "used": 0.0, "simulated": True})
        if parsed.path == "/v1/positions":
            return self.send_json({"account": account, "positions": [], "simulated": True})
        return self.send_json({"error": "unknown route"}, 404)

    def do_POST(self):
        return self.send_json({"error": "Read-only sandbox. Live order execution is disabled."}, 405)


def serve():
    server = ThreadingHTTPServer((HOST, PORT), GatewayHandler)
    print(f"WebAPI Bridge sandbox: http://{HOST}:{PORT}")
    print("Simulated data only; no real exchange requests.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    serve()
